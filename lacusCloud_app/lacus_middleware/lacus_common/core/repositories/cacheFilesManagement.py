
class cacheFilesManager:
    
    configFile = False
    cacheRootPath = ''
    cacheFileExtension = '.dat'
    resourcesRootPath = ''


    def createCacheFiles (self, fileInfo):
        raise NotImplementedError

    def deleteCacheFiles (self, fileInfo):
        raise NotImplementedError

    def getCacheFile (self, fileUID, chunkNumber):
        raise NotImplementedError

    def setChunkContent (self, fileUID, chunkNumber, content):
        raise NotImplementedError


    def restoreFileFromCache (self, fileInfo):
        raise NotImplementedError

    
    def copyFileIntoChunks (self, cachedFileInfo):
        raise NotImplementedError

    def writeChunkContent (self, content, fileName):
        raise NotImplementedError







    
