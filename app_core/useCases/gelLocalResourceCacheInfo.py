from ..interfaces.cacheDirectoryManagerInterface import cacheDirectoryManagerInterface
from ..interfaces.cacheFilesManagerInterface import cacheFilesManagerInterface
from ..interfaces.resourceDirectoryManagerInterface import resourceDirectoryManagerInterface
import threading


class getLocalResourceCacheInfo:

    cacheDirectoryManager = cacheDirectoryManagerInterface('')
    cacheFileManager = cacheFilesManagerInterface('', '')
    resourceDirectoryManagement = resourceDirectoryManagerInterface()
    resourceUID = False
    localHostIP = ''

    def __init__(self, cacheDirectoryManagerParam, cacheFileManagerParam, resourceDirectoryManagementParam , resourceUIDParam, localHostParam):
        super().__init__()
        self.cacheFileManager = cacheFileManagerParam
        self.cacheDirectoryManager = cacheDirectoryManagerParam
        self.resourceDirectoryManagement = resourceDirectoryManagementParam
        self.resourceUID = resourceUIDParam
        self.localHostIP = localHostParam
        

    def execute (self):
        cacheResourceInfo = self.cacheDirectoryManager.getCachedFileInfo(self.resourceUID)
        if (cacheResourceInfo == False):
            resourceInfo = self.resourceDirectoryManagement.getResourceInfo(False, self.resourceUID)
            if (resourceInfo == False):
                return False
            self.cacheDirectoryManager.createCacheDirectory(resourceInfo, self.localHostIP)
            cacheResourceInfo = self.cacheDirectoryManager.getCachedFileInfo(self.resourceUID)
            ### file thread Initiation
            fileManagementThread = cacheFileThread(self.cacheFileManager, cacheResourceInfo)
            fileManagementThread.start()
            ###
        return cacheResourceInfo


class cacheFileThread (threading.Thread):

    cacheFileManager = cacheFilesManagerInterface('','')
    fileInfo ={}

    def __init__(self, cacheFileManagerParam, fileInfoParam):
        super().__init__()
        self.cacheFileManager = cacheFileManagerParam
        self.fileInfo = fileInfoParam
    
    def run(self):
            self.cacheFileManager.createCacheFiles(self.fileInfo)