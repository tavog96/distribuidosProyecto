from ....lacus_common.core.common.interfaces.useCase import UseCase
from ..repositories.resourceDirectoryManagement import ResourceDirectoryManager
from ..repositories.nodeDirectoryManagement import NodeDirectoryManager


class GiveResourceInfo (UseCase):

    resourceManager = ResourceDirectoryManager()
    nodeManager = NodeDirectoryManager()

    ###Parameters
    resourceUid = False

    def __init__(self, resourceDirectoryManagement, nodeManager):
        super(GiveResourceInfo, self).__init__()
        self.nodeManager = nodeManager
        self.resourceManager = resourceDirectoryManagement

    def parameters(self, uid):
        self.resourceUid = uid
        
    
    def task(self):
        if (self.resourceUid != False):
            response = self.resourceManager.getResourceInfo(self.resourceUid)
            hostsCopy = []
            if ('host' in response):
                for host in response['host']:
                    hostsCopy.append(host)
            response['host'] = []
            for hostUid in hostsCopy:
                hostIp = self.nodeManager.getNodeIp(hostUid)
                if (hostIp != False):
                    response['host'].append(hostIp)
            self.response = response
        else:    
            self.response = False
        self.setDone()