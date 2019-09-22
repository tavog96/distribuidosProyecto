from ..interfaces.cacheDirectoryManagerInterface import cacheDirectoryManagerInterface


class getLocalResourceCacheInfo:

    cacheDirectoryManager = cacheDirectoryManagerInterface()
    resourceUID = False

    def __init__(self, cacheDirectoryManagerParam, resourceUIDParam, chunkNumberParam):
        super().__init__()
        self.cacheDirectoryManager = cacheDirectoryManagerParam
        self.resourceUID = resourceUIDParam
        self.chunkNumber = chunkNumberParam
        

    def execute (self):
        cacheResourceInfo = self.cacheDirectoryManager.getCachedFileInfo(self.resourceUID)
        if (cacheResourceInfo == False):
            return False
        return cacheResourceInfo