class cacheDirectoryManagerInterface:

    def __init__(self, cacheControlFileName):
        super().__init__()

    def createCacheDirectory (self, fileInfo, hostIP):
        raise NotImplementedError()

    def deleteCacheDirectory (self, fileUID):
        raise NotImplementedError()


    def getCachedFileInfo (self, fileUID):
        raise NotImplementedError()


    def appendFileInfo2CacheControlFile (self, fileInfo = False, hostIP = False):
        raise NotImplementedError()

    def calculateChunksNumber (self, size):
        raise NotImplementedError()
