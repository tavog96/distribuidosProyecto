from ....lacus_common.core.common.interfaces.useCase import UseCase
from ..repositories.cacheFilesManagement import cacheFilesManager
from ..repositories.restClient import restClientController

class DownloadResource (UseCase):

    cacheManager = cacheFilesManager()
    restController = restClientController(False, False)

    ###Parameters
    resourceUid = False
    resourceChunks = 0
    resourceHost = False
    resourceName = False

    hostCounter = 0

    def __init__(self, cacheManager, restController):
        super(DownloadResource, self).__init__()
        self.cacheManager = cacheManager
        self.restController = restController
        self.hostCounter = 0    

    def parameters(self, uid, chunks, host, name = False):
        self.resourceChunks = chunks
        self.resourceUid = uid
        self.resourceHost = host
        self.resourceName = name

    def nextHostIndex(self):
        if (len(self.resourceHost)>0):
            if (self.hostCounter < len(self.resourceHost)):
                if (self.hostCounter==(len(self.resourceHost)-1)):
                    self.hostCounter = 0
                else:
                    self.hostCounter = self.hostCounter+1
            else:
                self.hostCounter = 0

    
    def task(self):
        if (self.resourceHost!= False):
            chunkCounter = 1
            while (chunkCounter <= self.resourceChunks):
                self.restController.remoteHostIP = self.resourceHost[self.hostCounter]
                chunkContent = self.restController.getRemoteChunkFile(self.resourceUid, chunkCounter)
                if (chunkContent!= False):
                    self.cacheManager.setChunkContent(self.resourceUid, chunkCounter, chunkContent)
                    chunkCounter = chunkCounter+1
                    self.progress = int((chunkCounter/self.resourceChunks)*100)
                self.nextHostIndex()
            self.result = True
            if (self.resourceName!=False):
                fileInfo= {}
                fileInfo['uid'] = self.resourceUid
                fileInfo['name'] = self.resourceName
                fileInfo['chunks'] = self.resourceChunks
                self.cacheManager.restoreFileFromCache(fileInfo)
        self.setDone()




    