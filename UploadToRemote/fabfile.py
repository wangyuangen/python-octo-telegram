# -*- coding:gbk -*-

import os
import json
import time
from fabric.api import *

try:
    with open('%s/ServiceConfig.txt' % os.path.abspath('.'),'r') as f:
        service_str = f.read()
        service_config = json.loads(service_str)
except IOError as err:
    print "ServiceConfig.txt δ�ҵ�"
    print "Error :%s" % str(err)
    
env.shell="cmd.exe /c"
env.always_use_pty = False
env.roledefs = service_config["roledefs"]
env.passwords = service_config["passwords"]
logResult = []

def put_file(localPath,remotePath):
    # print (env)
    result = put(localPath,remotePath)
    if result.failed:
        print u"\n--------%s �ϴ��� %s ʧ��--------\n" % (localPath,remotePath)
        logResult.append(u'%s %s �ϴ��� %s ʧ�� IP:%s' % (time.strftime("%y-%m-%d %H:%M:%S"),localPath,remotePath,env.host_string))
    else:
        print u"\n--------%s �ϴ��� %s �ɹ�--------\n" % (localPath,remotePath)
        logResult.append(u'%s %s �ϴ��� %s �ɹ� IP:%s' % (time.strftime("%y-%m-%d %H:%M:%S"),localPath,remotePath,env.host_string))

# ����: roles=hotfix,path = C:/LinKedCare/HotFixDeploy/files/,version=2.1.4
def deploy(path='C:/LinKedCare/HotFixDeploy/files/',version='1.0.1'):
    try:
        with open('%s/PathConfig.txt' % path,'r') as f:
            path_str = f.read()
            path_config = json.loads(path_str)
    except IOError as err:
        print "PathConfig.txt δ�ҵ�"
        print "Error :%s" % str(err)
    run('c:/StopIIS.bat')   # stop iis service
    for item in path_config:
        filepath = path + item
        put_file(filepath,path_config[item])
        
    run('c:/StartIIS.bat')  # start iis service
    logResultDir = os.path.abspath('.')+'\DeployLog'
    if os.path.exists(logResultDir) == False:
        os.mkdir(logResultDir)
    filename = '\%s_log.txt' % version
    filepath = '%s%s' % (logResultDir,filename)
    with open(filepath,'w') as f:
        for log in logResult:
            f.write(log.encode('utf-8'))
            f.write("\n")
        print 'д����־��%s' % filepath

#deploy('C:/LinKedCare/HotFixDeploy/files/','2.1.4')
