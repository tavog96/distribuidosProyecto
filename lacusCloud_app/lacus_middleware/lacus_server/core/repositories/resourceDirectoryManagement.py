

class ResourceDirectoryManager:
    
    def addResource (self, fileInfo):
        raise NotImplementedError


    def getResourceInfo (self, fileUID):
        raise NotImplementedError

    def getResourceList (self):
        raise NotImplementedError

    def appendFileInfo2CacheControlFile (self, fileInfo = False):
        raise NotImplementedError

    def calculateChunksNumber (self, size):
        raise NotImplementedError

    def addHostToResource (self, uid, host):
        raise NotImplementedError



