from ..interfaces.resourceDirectoryManagerInterface import resourceDirectoryManagerInterface

class getLocalResourceList:

    resourceDirectoryManager = resourceDirectoryManagerInterface(False, False,False)

    def __init__(self, resourceDirectoryManagerParam):
        super().__init__()
        self.resourceDirectoryManager = resourceDirectoryManagerParam

    def execute (self):
        localResourceDirectory = self.resourceDirectoryManager.getResourcesInfo()
        return localResourceDirectory