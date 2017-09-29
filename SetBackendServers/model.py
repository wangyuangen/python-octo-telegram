
class ResponseBase():
    def __init__(self):
        self.RequestId = ''
        self.HostId = ''
        self.Code = ''
        self.Message = ''

class DescribeHealth(ResponseBase):
    def __int__(self):
        self.BackendServers = ''

class BackendDescribes():
    def __int__(self):
        self.ServerId = ''
        self.ServerHealthStatus = ''

class BackendServersRep(ResponseBase):
    def __int__(self):
        self.LoadBalancerId = ''
        self.BackendServers = ''

class BackendServers():
    def __int__(self):
        self.ServerId=''
        self.Weight = 0