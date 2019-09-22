class restClientControllerInterface:

    def __init__(self, defaultPort, remoteHostIP):
        super().__init__()

    
    def getRemoteResourceList (self):
        raise NotImplementedError()

    def getRemoteResourceCacheInfo (self, uidParam):
        raise NotImplementedError()


    def getRemoteChunkFile (self, uidParam, chunkNumber):
        raise NotImplementedError()