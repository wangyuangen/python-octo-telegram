
class ResponseBase():
    def __init__(self):
        self.RequestId = ''
        self.HostId = ''
        self.Code = ''
        self.Message = ''

class DescribeHealth(ResponseBase):
    def __init__(self):
        self.BackendServers = ''

class BackendDescribes():
    def __init__(self):
        self.ServerId = ''
        self.ServerHealthStatus = ''

class BackendServersRep(ResponseBase):
    def __init__(self):
        self.LoadBalancerId = ''
        self.BackendServers = ''

class BackendServers():
    def __init__(self):
        self.ServerId=''
        self.Weight = 0
