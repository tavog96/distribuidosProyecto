from ..interfaces.cacheDirectoryManagerInterface import cacheDirectoryManagerInterface
from ..interfaces.cacheFilesManagerInterface import cacheFilesManagerInterface


class getLocalResourceChunk:

    cacheDirectoryManager = cacheDirectoryManagerInterface()
    cacheFilesManager = cacheFilesManagerInterface()
    resourceUID = False
    chunkNumber = 0

    def __init__(self, cacheDirectoryManagerParam, cacheFilesManagerParam, resourceUIDParam, chunkNumberParam):
        super().__init__()
        self.cacheDirectoryManager = cacheDirectoryManagerParam
        self.cacheFilesManager = cacheFilesManagerParam
        self.resourceUID = resourceUIDParam
        self.chunkNumber = chunkNumberParam
        

    def execute (self):
        cacheResourceInfo = self.cacheDirectoryManager.getCachedFileInfo(self.resourceUID)
        if (cacheResourceInfo == False):
            return False
        if (self.chunkNumber<=0 or self.chunkNumber>cacheResourceInfo['chunks']):
            return False
        chunkContent = self.cacheFilesManager.getCacheFile(self.resourceUID, self.chunkNumber)
        return chunkContent

        