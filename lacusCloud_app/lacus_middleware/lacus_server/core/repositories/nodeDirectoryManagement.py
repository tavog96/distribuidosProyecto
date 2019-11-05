
class NodeDirectoryManager:


    def updateNode(self, hostIp, hostUid):
        raise NotImplementedError
        

    def getNodeIp (self, hostUid):
        raise NotImplementedError


    def removeNode (self, hostUid):
        raise NotImplementedError


    def getAllNodes (self):
        raise NotImplementedError


    def createEmptyDirectory (self):
        raise NotImplementedError




