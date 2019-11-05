from ....lacus_common.core.common.interfaces.useCase import UseCase
from ..repositories.nodeDirectoryManagement import NodeDirectoryManager

class RegisterNode (UseCase):

    nodeManager = NodeDirectoryManager()

    ###Parameters
    hostIp = False
    hostUid = False

    def __init__(self, nodeManager):
        super(RegisterNode, self).__init__()
        self.nodeManager = nodeManager

    def parameters(self, uid, ip):
        self.hostIp = ip
        self.hostUid = uid
        
    
    def task(self):
        self.response = self.nodeManager.updateNode(self.hostIp, self.hostUid)
        self.setDone()
        
    