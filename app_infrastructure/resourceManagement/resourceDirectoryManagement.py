from .resourceDirectoryScan import filesScaner
from ..jsonFileController.jsonSave import jsonSaver
from .resourceIntegrityControl import integrityMonitor

class resourceDirectoryManager:
    
    directoryFileName = ''
    directoryRootPath = ''
    scanner = filesScaner()
    jsonSaver = jsonSaver()
    integrityCheker = integrityMonitor()

    def __init__(self, directoryFileName = 'filesDir.json', directoryRootPath = './files', versionControl= False):
        super().__init__()
        self.directoryFileName = directoryFileName
        self.directoryRootPath = directoryRootPath
        self.scanner = filesScaner(self.directoryRootPath)
        self.jsonSaver = jsonSaver(self.directoryFileName)
        self.integrityCheker =  integrityMonitor(versionControl)

    def scanDirectory(self):
        scannedFilesDir = self.scanner.filesInfoScan()
        savedFilesDir = self.jsonSaver.openJson()
        lastVersionDirectory = self.integrityCheker.integrityVerification(savedFilesDir, scannedFilesDir)
        self.jsonSaver.saveJson(lastVersionDirectory)
        return lastVersionDirectory

    def getResourceInfo (self, fileName = False, fileUID = False):
        savedFilesDir = self.jsonSaver.openJson()
        for fileInfo in savedFilesDir:
            if (fileName!=False):
                if (fileInfo['name']==fileName):
                    return fileInfo
            if (fileUID!=False):
                if (fileInfo['uid']==fileUID):
                    return fileInfo
        return False

    def getResourcesInfo (self):
        savedFilesDir = self.jsonSaver.openJson()
        return savedFilesDir

    def setResourceInfo (self, resourceInfo):
        savedFilesDir = self.jsonSaver.openJson()
        indexCounter = 0
        flagFound = False
        while indexCounter < len(savedFilesDir):
            if (savedFilesDir[indexCounter]['name']==resourceInfo['name']):
                savedFilesDir[indexCounter] = resourceInfo
                flagFound=True
        if (not flagFound):
            savedFilesDir.append(resourceInfo)
        self.jsonSaver.saveJson(savedFilesDir)
