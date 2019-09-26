from ..interfaces.resourceDirectoryManagerInterface import resourceDirectoryManagerInterface
from ..interfaces.restClientControllerInterface import restClientControllerInterface

class getLocalResourceList:

    resourceDirectoryManager = resourceDirectoryManagerInterface()
    restClientController = restClientControllerInterface(False, False)


    def __init__(self, resourceDirectoryManagerParam, restClientControllerParam):
        super().__init__()
        self.resourceDirectoryManager = resourceDirectoryManagerParam
        self.restClientController = restClientControllerParam

    def execute (self):
        remoteResourceList = self.restClientController.getRemoteResourceList()
        if remoteResourceList == False:
            return False
        localResourceList = self.resourceDirectoryManager.getResourcesInfo()
        if (localResourceList != False):
            for localResource in localResourceList:
                for remoteResource in remoteResourceList:
                    if (localResource['uid']==remoteResource['uid']):
                        remoteResource['onLocal'] = True
                        break
        return remoteResourceList