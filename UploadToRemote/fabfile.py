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
    print "ServiceConfig.txt 未找到"
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
        print u"\n--------%s 上传到 %s 失败--------\n" % (localPath,remotePath)
        logResult.append(u'%s %s 上传到 %s 失败 IP:%s' % (time.strftime("%y-%m-%d %H:%M:%S"),localPath,remotePath,env.host_string))
    else:
        print u"\n--------%s 上传到 %s 成功--------\n" % (localPath,remotePath)
        logResult.append(u'%s %s 上传到 %s 成功 IP:%s' % (time.strftime("%y-%m-%d %H:%M:%S"),localPath,remotePath,env.host_string))

# 参数: roles=hotfix,path = C:/LinKedCare/HotFixDeploy/files/,version=2.1.4
def deploy(path='C:/LinKedCare/HotFixDeploy/files/',version='1.0.1'):
    try:
        with open('%s/PathConfig.txt' % path,'r') as f:
            path_str = f.read()
            path_config = json.loads(path_str)
    except IOError as err:
        print "PathConfig.txt 未找到"
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
        print '写入日志到%s' % filepath

#deploy('C:/LinKedCare/HotFixDeploy/files/','2.1.4')
