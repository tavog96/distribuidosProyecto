class cacheFilesManagerInterface:
    

    def __init__(self, cacheRootPath, resourcesRootPath):
        super().__init__()


    def createCacheFiles (self, fileInfo):
        raise NotImplementedError()

    def deleteCacheFiles (self, fileInfo):
        raise NotImplementedError()

    def getCacheFile (self, fileUID, chunkNumber):
        raise NotImplementedError()

    def restoreFileFromCache (self, fileInfo):
        raise NotImplementedError()
    
    def copyFileIntoChunks (self, cachedFileInfo):
        raise NotImplementedError()

    def writeChunkContent (self, content, fileName):
        raise NotImplementedError()
