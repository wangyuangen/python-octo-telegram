import sys,os
import urllib,urllib2
import base64
import hmac
import time
import uuid
import json
import datetime
import oss2
import ConfigParser
from hashlib import sha1
from Logger import GetLog

config = ConfigParser.ConfigParser()
config.read("config.ini")
api_host_uri = config.get('api','api_host_uri')
access_key_id = config.get('api','access_key_id')
access_key_secret =  config.get('api','access_key_secret')
oss_end_point =  config.get('oss','oss_end_point')
oss_file_path =  config.get('oss','oss_file_path')
oss_access_keyId =  config.get('oss','oss_access_keyId')
oss_access_keysecret = config.get('oss','oss_access_keysecret')
oss_access_bucketname =  config.get('oss','oss_access_bucketname')

class ResponseBase:
    def __init__(self):
        self.RequestId = ''
        self.HostId = ''
        self.Code = ''
        self.Message = ''

class BinLogFile:
    def __init__(self):
        self.FileSize = 0
        self.LogBeginTime = ''
        self.LogEndTime = ''
        self.DownloadLink = ''
        self.HostInstanceID = ''
        self.LinkExpiredTime = ''
        self.IntranetDownloadLink = ''
        self.Checksum = ''

class BinLogFileResponse(ResponseBase):
    def __init__(self):
        self.TotalRecordCount = 0
        self.PageNumber = 0
        self.PageRecordCount = 0
        self.TotalFileSize = ''
        self.Items = ''

def percent_encode(encodeStr):
    encodeStr = str(encodeStr)
    res = urllib.quote(encodeStr.decode('utf8').encode('utf8'),'')
    res = res.replace('+','%20')
    res = res.replace('*','%2A')
    res = res.replace('%7E','~')
    return  res

def compute_signature(parameters,access_key_secret):
    sortedParameters = sorted(parameters.items(),key=lambda parameters:parameters[0])
    canonicalizedQueryString = ''
    for (k,v) in sortedParameters:
        canonicalizedQueryString += '&' + percent_encode(k) +'='+percent_encode(v)
    stringToSign = 'GET&%2F&' + percent_encode(canonicalizedQueryString[1:])
    h = hmac.new(access_key_secret+'&',stringToSign,sha1)
    signature = base64.encodestring(h.digest()).strip()
    return signature

def compose_url(user_params):
    timestamp = time.strftime("%Y-%m-%dT%H:%M:%SZ",time.gmtime(time.time()))
    parameters ={\
        'Format':'JSON',\
        'Version':'2014-08-15',\
        'AccessKeyId':access_key_id,\
        'SignatureVersion':'1.0',\
        'SignatureMethod':'HMAC-SHA1',\
        'SignatureNonce':str(uuid.uuid1()),\
        'TimeStamp':timestamp\
    }
    for key in user_params.keys():
        parameters[key] = user_params[key]
    signature = compute_signature(parameters,access_key_secret)
    parameters['Signature'] = signature
    url = api_host_uri+'/?'+urllib.urlencode(parameters)
    return url

def make_request(user_params,quiet=False):
    url = compose_url(user_params)
    request = urllib2.Request(url)
    try:
        conn = urllib2.urlopen(request)
        response = conn.read()
    except urllib2.HTTPError,e:
        log.error(e)
        raise SystemExit(e)
    try:
        obj = json.loads(response)
        if quiet:
            return  obj
    except ValueError,e:
        log.error(e)
        raise SystemExit(e)
    json.dump(obj,sys.stdout,sort_keys=True,indent=2)
    sys.stdout.write('\n')

def GetDownloadLinks(dbinstance,starttime,endtime):
    user_params = {
        'Action': 'DescribeBinlogFiles',
        'DBInstanceId': dbinstance,
        'PageSize': 100,
        'PageNumber': 1,
        'StartTime': starttime,
        'EndTime': endtime
    }
    response = make_request(user_params,True)
    binlogFiles = BinLogFileResponse()
    binlogFiles.__dict__ = response
    return binlogFiles

def UploadBinlogFile():
    index = 0
    starttime = datetime.datetime.strftime(datetime.datetime.now() + datetime.timedelta(days=-1),
                                           "%Y-%m-%dT%H:%M:%SZ")
    endtime = datetime.date.strftime(datetime.datetime.now(), "%Y-%m-%dT%H:%M:%SZ")
    log.info('startTime:{0}   endTime:{1}'.format(starttime,endtime))
    timeStamp = datetime.date.strftime(datetime.datetime.now(),"%Y%m%d")
    for dbinstance in dbInstanceIds:
        log.info('dbInstanceId:{0}'.format(dbinstance))
        downloadLinks = GetDownloadLinks(dbinstance,starttime,endtime)
        auth = oss2.Auth(oss_access_keyId,oss_access_keysecret)
        bucket = oss2.Bucket(auth,oss_end_point,oss_access_bucketname)
        log.info('file totalcount:{0}'.format(downloadLinks.TotalRecordCount))
        for item in downloadLinks.Items.values()[0]:
            index = index+1
            log.info('-------------------- file index of {0} --------------------'.format(index))
            binlogfile = BinLogFile()
            binlogfile.__dict__ = item
            link = binlogfile.DownloadLink
            filename = oss_file_path +timeStamp+'_'+ str(index) +'_'+link[link.rfind('/')+1:link.find('?')]
            log.info('file name:{0}'.format(filename))
            try:
                f = urllib2.urlopen(link)
                # data = f.read()
                result = bucket.put_object(filename,f.read())
            except Exception,e:
                log.error(e)
            else:
                log.info('http status: {0}'.format(result.status))
                log.info('request_id: {0}'.format(result.request_id))
                log.info('Etag: {0}'.format(result.etag))
                log.info('Date: {0}'.format(result.headers['date']))

def DeleteBinlogFile():
    deleteIndex = 0
    day = int(datetime.date.strftime(datetime.datetime.now()+datetime.timedelta(days=-90),
                                     "%Y%m%d"))
    auth = oss2.Auth(oss_access_keyId, oss_access_keysecret)
    bucket = oss2.Bucket(auth, oss_end_point, oss_access_bucketname)
    for b in oss2.ObjectIterator(bucket,prefix=oss_file_path+'2'):
        path = b.key
        fileName = path[path.rfind('/')+1:path.find('.')]
        startWith = int(fileName[0:fileName.find('_')])
        if startWith<day:
            try:
                bucket.delete_object(path)
            except Exception,e:
                log.error(e)
            else:
                deleteIndex = deleteIndex + 1
    log.info('Delete 90 days ago -- File Count:{0}'.format(deleteIndex))

options =  config.options('rds')
dbInstanceIds = [];
for opt in options:
    dbInstanceIds.append(config.get('rds',opt))

log = GetLog()
DeleteBinlogFile()
UploadBinlogFile()
