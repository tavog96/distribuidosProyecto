from ....lacus_common.infrastructure.jsonFileController.jsonSave import jsonSaver
from ....lacus_common.infrastructure.configFileController.configFileController import configFileController
import time
import uuid

class ResourceDirectoryManager:
    
    resourceDirectoryFileName = False
    chunkSize = 1048576 ## 1 MB
    configController = configFileController ()
    jsonFile = jsonSaver()

    def __init__(self):
        super().__init__()
        self.configController.scanConfigFile()
        self.resourceDirectoryFileName = configFileController.resourceDirectoryFileName
        self.jsonFile = jsonSaver(self.resourceDirectoryFileName)

    def addResource (self, fileInfo):
        if (fileInfo != False):
            fileInfo['uid'] = str(uuid.uuid1())
            return self.appendFileInfo2CacheControlFile(fileInfo)
        return False


    def getResourceInfo (self, fileUID):
        savedCachedFilesInfo = self.jsonFile.openJson()
        if (savedCachedFilesInfo != False):
            if (fileUID!=False and fileUID!=""):
                for fileInfo in savedCachedFilesInfo:
                    if (fileInfo['uid']==fileUID):
                        return fileInfo
            return False
        return False

    def getResourceList (self):
        resourceFileInf = self.jsonFile.openJson()
        if (resourceFileInf == False):
            resourceFileInf=[]
        for resource in resourceFileInf:
            resource.pop('chunks')
            resource.pop('uploadDate')
            resource.pop('chunkSize')
            if ('host' in resource):
                resource.pop('host')
        return resourceFileInf

    def appendFileInfo2CacheControlFile (self, fileInfo = False):
        fileInfo2Appen = {}
        if (fileInfo == False):
            return False
        savedCachedFilesInfo = self.jsonFile.openJson()
        if (savedCachedFilesInfo == False):
            savedCachedFilesInfo=[]
        fileInfo2Appen['uid'] = fileInfo['uid']
        fileInfo2Appen['name'] = fileInfo['name']
        fileInfo2Appen['size'] = fileInfo['size']
        fileInfo2Appen['lastmodificate'] = fileInfo['lastmodificate']
        tempChunks = self.calculateChunksNumber(fileInfo['size'])
        fileInfo2Appen['chunks'] = tempChunks
        fileInfo2Appen['uploadDate'] = time.time()
        fileInfo2Appen['chunkSize'] = self.chunkSize
        savedCachedFilesInfo.append(fileInfo2Appen)
        self.jsonFile.saveJson(savedCachedFilesInfo)
        return fileInfo2Appen

    def addHostToResource (self, uid, host):
        savedCachedFilesInfo = self.jsonFile.openJson()
        if (savedCachedFilesInfo != False):
            if (uid!=False and uid!=""):
                for fileInfo in savedCachedFilesInfo:
                    if (fileInfo['uid']==uid):
                        if (not 'host' in fileInfo):
                            fileInfo['host'] = []
                        fileInfo['host'].append(host)
                        self.jsonFile.saveJson(savedCachedFilesInfo)
                        return True
            return False
        return False


    def calculateChunksNumber (self, size):
        chunks = int(size/self.chunkSize)
        residue = size%self.chunkSize
        if (residue>0):
            chunks = (chunks + 1)
        return chunks



