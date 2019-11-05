from ..jsonFileController.jsonSave import jsonSaver
from ..configFileController.configFileController import configFileController
import time
import os

class cacheFilesManager:
    
    configFile = configFileController()
    cacheRootPath = ''
    cacheFileExtension = '.dat'
    resourcesRootPath = ''

    def __init__(self, cacheRootPath, resourcesRootPath):
        super().__init__()
        self.configFile.scanConfigFile()
        self.cacheRootPath = self.configFile.cachePathRoot
        self.resourcesRootPath = self.configFile.resourcePathRoot

    def deleteCacheFiles (self, fileInfo):
        if fileInfo!= False:
            counter =1
            while counter <= fileInfo['chunks']:
                chunkFileName = self.cacheRootPath+fileInfo['uid']+'_'+str(counter)+self.cacheFileExtension
                if os.path.exists(chunkFileName):
                    os.remove(chunkFileName)
                else:
                    print("The file does not exist") 
                counter = counter+1
            return True
        return False

    def getCacheFile (self, fileUID, chunkNumber):
        fileName = fileUID+'_'+str(chunkNumber)+self.cacheFileExtension
        if not os.path.exists(self.cacheRootPath + fileName):
            return False
        chunkFile = open(self.cacheRootPath+fileName, 'rb')
        fileContent = chunkFile.read()
        chunkFile.close()
        return fileContent

    def setChunkContent (self, fileUID, chunkNumber, content):
        filename = fileUID+'_'+str(chunkNumber)+self.cacheFileExtension
        self.writeChunkContent(content, filename)


    def restoreFileFromCache (self, fileInfo):
        fileName = fileInfo['name']
        chunks = fileInfo['chunks']
        chunkCounter = 1
        nameCounter = 1
        while (os.path.exists(self.resourcesRootPath + fileName)):
            fileName = '('+str(nameCounter)+')'+fileInfo['name']
            nameCounter = nameCounter+1

        file2write = open(self.resourcesRootPath + fileName,'wb')

        while (chunkCounter<=chunks):
            chunkContent = self.getCacheFile(fileInfo['uid'], chunkCounter)
            if (chunkContent!=False):
                file2write.write(chunkContent)
        file2write.close()
        return fileName

    
    def copyFileIntoChunks (self, cachedFileInfo, path):
        chunks = cachedFileInfo['chunks']
        chunkCounter= 1

        if not os.path.exists(path):
            return False

        file2read = open(path, 'rb')

        while (chunkCounter<=chunks):
            bytes2Read = cachedFileInfo['chunkSize']
            if (chunkCounter==chunks):
                bytes2Read = int(cachedFileInfo['size']%cachedFileInfo['chunkSize'])
            chunkContent = file2read.read(bytes2Read)
            filename = cachedFileInfo['uid']+'_'+str(chunkCounter)+self.cacheFileExtension
            self.writeChunkContent(chunkContent, filename)
            chunkCounter = chunkCounter+1

    def writeChunkContent (self, content, fileName):
        file2save = open(self.cacheRootPath+fileName, 'wb')
        file2save.write(content)
        file2save.close()







    
