import sys
import urllib,urllib2
import json
import base64
import time
import hmac
import uuid
import ConfigParser
from hashlib import sha1
from logger import GetLog

config = ConfigParser.ConfigParser()
config.read('config.ini')
api_host_uri = config.get('api','api_host_uri')
access_key_id = config.get('api','access_key_id')
access_key_secret =  config.get('api','access_key_secret')
slb_id = config.get('slb','serverid')
maintain_id = config.get('maintain','serverid')

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
        'Version':'2014-05-15',\
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

log = GetLog()