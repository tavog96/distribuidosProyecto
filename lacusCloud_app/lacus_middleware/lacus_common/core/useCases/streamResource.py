from ....lacus_common.core.common.interfaces.useCase import UseCase
from ..repositories.cacheFilesManagement import cacheFilesManager

class StreamResource (UseCase):

    ###Parameters
    resourceUid = False
    resourceChunk = False
    cacheManager = cacheFilesManager()

    def __init__(self, cacheManager):
        super(StreamResource, self).__init__()
        self.cacheManager =  cacheManager

    def parameters(self, uid, chunk):
        self.resourceChunk = chunk
        intchunk = chunk
        try:
            intchunk = int(chunk)
        except:
            pass
        self.resourceUid = uid
    
    def task(self):
        if (self.resourceUid!=False and self.resourceChunk!= False):
            chunkContent = self.cacheManager.getCacheFile(self.resourceUid, self.resourceChunk)
            self.response = chunkContent
            self.setDone()
            return True
        self.response =  False
        self.setDone()
    