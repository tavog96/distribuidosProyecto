from ..jsonFileController.jsonSave import jsonSaver
from ..resourceManagement.resourceDirectoryManagement import resourceDirectoryManager
import time


class cacheDirectoryManager:
    
    cacheControlFileName = ''
    chunkSize = 1048576 ## 1 MB
    jsonCacheControlFile = jsonSaver()

    def __init__(self, cacheControlFileName):
        super().__init__()
        self.cacheControlFileName=cacheControlFileName
        self.jsonCacheControlFile = jsonSaver(self.cacheControlFileName)

    def createCacheDirectory (self, fileInfo, hostIP):
        if (fileInfo != False):
            cachedFileInfo = self.getCachedFileInfo(fileInfo['uid'])
            if (cachedFileInfo == False):
                ## crear el registro cache
                return self.appendFileInfo2CacheControlFile(fileInfo, hostIP)
            return True
        return False

    def deleteCacheDirectory (self, fileUID):
        pass


    def getCachedFileInfo (self, fileUID):
        savedCachedFilesInfo = self.jsonCacheControlFile.openJson()
        if (savedCachedFilesInfo != False):
            if (fileUID!=False and fileUID!=""):
                for fileInfo in savedCachedFilesInfo:
                    if (fileInfo['uid']==fileUID):
                        return fileInfo
            return False
        return False


    def appendFileInfo2CacheControlFile (self, fileInfo = False, hostIP = False):
        fileInfo2Appen = {}
        if (fileInfo == False):
            return False
        savedCachedFilesInfo = self.jsonCacheControlFile.openJson()
        if (savedCachedFilesInfo == False):
            savedCachedFilesInfo=[]
        fileInfo2Appen['uid'] = fileInfo['uid']
        fileInfo2Appen['name'] = fileInfo['name']
        fileInfo2Appen['size'] = fileInfo['size']
        tempChunks = self.calculateChunksNumber(fileInfo['size'])
        fileInfo2Appen['chunks'] = tempChunks
        fileInfo2Appen['cachedDate'] = time.time()
        fileInfo2Appen['chunkSize'] = self.chunkSize
        if (hostIP!=False):
            hosts = []
            hosts.append(hostIP)
            fileInfo2Appen['hosts']=hosts
        savedCachedFilesInfo.append(fileInfo2Appen)
        self.jsonCacheControlFile.saveJson(savedCachedFilesInfo)
        return fileInfo2Appen

    def calculateChunksNumber (self, size):
        chunks = int(size/self.chunkSize)
        residue = size%self.chunkSize
        if (residue>0):
            chunks = (chunks + 1)
        return chunks







    
