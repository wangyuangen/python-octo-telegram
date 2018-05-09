import sys,os
import urllib,urllib2
import base64
import datetime
import time
import hmac
import json
import uuid
import ConfigParser
from hashlib import sha1
from logger import GetLog

config = ConfigParser.ConfigParser()
config.read("config.ini")
api_host_uri = config.get('api','api_host_uri')
access_key_id = config.get('api','access_key_id')
access_key_secret =  config.get('api','access_key_secret')

class ResponseBase:
    def __init__(self):
        self.RequestId = ''
        self.HostId = ''
        self.Code = ''
        self.Message = ''

class CheckBackupRep(ResponseBase):
    def __init__(self):
        self.TotalRecordCount = 0
        self.PageNumber = 0
        self.PageRecordCount = 0
        self.Items = ''

class Backup:
    def __init__(self):
        self.BackupId = 0
        self.DBInstanceId = ''
        self.HostInstanceID = ''
        self.BackupStatus = ''
        self.BackupStartTime = ''
        self.BackupEndTime = ''
        self.BackupType = ''
        self.BackupMode = ''
        self.BackupMethod = ''
        self.BackupDownloadURL = ''
        self.BackupIntranetDownloadURL = ''
        self.BackupSize = 0
        self.StoreStatus = ''

def percent_encode(encodeStr):
    encodeStr = str(encodeStr)
    res = urllib.quote(encodeStr.decode('utf8').encode('utf8'), '')
    res = res.replace('+', '%20')
    res = res.replace('*', '%2A')
    res = res.replace('%7E', '~')
    return res

def compute_signature(parameters,access_key_secret):
    sortedParameters = sorted(parameters.items(), key=lambda parameters: parameters[0])
    canonicalizedQueryString = ''
    for (k, v) in sortedParameters:
        canonicalizedQueryString += '&' + percent_encode(k) + '=' + percent_encode(v)
    stringToSign = 'GET&%2F&' + percent_encode(canonicalizedQueryString[1:])
    h = hmac.new(access_key_secret + '&', stringToSign, sha1)
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

def createBackup(dbinstance):
    request={
        'Action':'CreateBackup',
        'DBInstanceId':dbinstance,
        'BackupMethod':'Physical',  #'Logical/Physical'
        'BackupType':'Auto' #'Auto/FullBackup'
    }
    log.info('Start Backup For RdsId:{0}'.format(dbinstance))
    response = make_request(request,True)
    rep = ResponseBase()
    rep.__dict__ = response
    try:
        log.error('Code:{0}  Message:{1}'.format(rep.Code,rep.Message))
    except Exception,e:
        log.info("Backup in progress...")

def checkBackup(dbinstance):
    startTime = datetime.datetime.strftime(datetime.datetime.utcnow() - datetime.timedelta(hours=1),
                                           "%Y-%m-%dT%H:%MZ")
    endTime = datetime.datetime.strftime(datetime.datetime.utcnow()+ datetime.timedelta(hours=1),
                                     "%Y-%m-%dT%H:%MZ")
    while True:
        request = {
            'Action':'DescribeBackups',
            'DBInstanceId':dbinstance,
            'StartTime':startTime,
            'EndTime':endTime,
            'PageSize':100,
            'PageNumber':1
        }
        response = make_request(request,True)
        rep = CheckBackupRep()
        rep.__dict__ = response
        successNum = 0
        totalNum = 0
        for item in rep.Items.values()[0]:
            totalNum = totalNum + 1
            backup = Backup()
            backup.__dict__ = item
            if backup.BackupStatus == 'Success':
                successNum = successNum + 1
        if totalNum != 0 and totalNum == successNum:
            log.info('rds backup success:{0}'.format(dbinstance))
            break


def main():
    for dbinstance in dbInstanceIds:
        createBackup(dbinstance)
    for dbinstance in dbInstanceIds:
        checkBackup(dbinstance)

options =  config.options('rds')
dbInstanceIds = [];
for opt in options:
    dbInstanceIds.append(config.get('rds',opt))

log = GetLog()
main()
