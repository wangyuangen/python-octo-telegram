import random
from model import *
from comman import *
from logger import GetLog

def DescribeHealthStatus():
    parameter={
        'Action':'DescribeHealthStatus',
        # 'RegionId':''
        'ListenerPort':80,
        'LoadBalancerId':slb_id
    }
    response = make_request(parameter,True)
    rep = DescribeHealth()
    rep.__dict__ = response
    return rep

def AddBackendServers():
    backendServers = []
    parameter = {
        #'ServerId':'it-estrdsserverid',
        #'Weight':100
    }
    backendServers.append(parameter)
    jsonStr = json.dumps(backendServers)
    parameter = {
        'Action':'AddBackendServers',
        'LoadBalancerId':slb_id,
        'BackendServers':jsonStr,
    }
    response = make_request(parameter,True)
    rep = BackendServersRep()
    rep.__dict__ = response

def SetBackendServers(BackendServers):
    jsonStr = json.dumps(BackendServers)
    parameter = {
        'Action':'SetBackendServers',
        #'RegionId':'',
        'LoadBalancerId':slb_id,
        'BackendServers':jsonStr
    }
    response = make_request(parameter,True)
    rep = BackendServersRep()
    rep.__dict__ = response
    return rep

def StopOrStart(weight):
    describes = DescribeHealthStatus().BackendServers.values()[0]
    BackendServers = []
    for item in describes:
        backend = BackendDescribes()
        backend.__dict__ = item
        if backend.ServerId == maintain_id:
            param = {
                'ServerId': backend.ServerId,
                'Weight': weight
            }
        else:
            param = {
                'ServerId': backend.ServerId,
                'Weight': 100 - weight
            }
        BackendServers.append(param)
    return SetBackendServers(BackendServers)

def RandomSelection(weight):
    describes = DescribeHealthStatus().BackendServers.values()[0]
    randomServer = random.sample(describes,1)[0]
    server = BackendDescribes()
    server.__dict__ = randomServer
    BackendServers= []
    for item in describes:
        backend = BackendDescribes()
        backend.__dict__ = item
        if backend.ServerId == server.ServerId:
            param = {
                'ServerId': backend.ServerId,
                'Weight': 100
            }
        else:
            param = {
                'ServerId': backend.ServerId,
                'Weight': 100-weight
            }
        BackendServers.append(param)
    return  SetBackendServers(BackendServers)

def Main(arg):
    if arg.lower() == 'stop':
       log.info('Set Backend Servers - Stop')
       response = StopOrStart(100)
    elif arg.lower() == 'start':
       log.info('Set Backend Servers - Start')
       response = StopOrStart(0)
    elif arg.lower() == 'random':
        log.info('Set Backend Servers - Random')
        response = RandomSelection(100)
    elif arg.lower() == 'restore':
        log.info('Set Backend Servers - Restore')
        response = RandomSelection(0)
    log.info('----------------Change Result----------------')
    log.info('SLB-ServerId:{0}'.format(response.LoadBalancerId))
    for server in response.BackendServers['BackendServer']:
        backend = BackendServers()
        backend.__dict__ = server
        log.info('ESC-ServerId:{0}  Weight:{1}'.format(backend.ServerId,backend.Weight))
    log.info('Set Backend Servers Finish')

log = GetLog()

