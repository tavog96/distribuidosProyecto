from ...lacus_common.infrastructure.networkManagement.restClient import restClientController
from ...lacus_common.infrastructure.configFileController.configFileController import configFileController
from ..infrastructure.fileManagement.fileManager import FileManager
from ...lacus_common.infrastructure.cacheManagement.cacheFilesManagement import cacheFilesManager
from ...lacus_common.core.useCases.downloadResource import DownloadResource
from .restServer.serverController import ClientController
from threading import Thread
import time
import json

class Client:

    trackerIP = False
    sessionToken = False
    configFile = configFileController()
    downloader = DownloadResource(False, False)
    clientServer = ClientController()
    clientServerThread = Thread(target=False)


    def __init__(self, localHostIP, trackerIP):
        super().__init__()
        self.configFile.scanConfigFile()
        self.trackerIP = trackerIP
        self.configFile.localHostIP = localHostIP
        self.configFile.setDefaultConfigFile()
        self.clientServerThread = Thread(target=self.startServer)
        self.clientServerThread.start()

    def login(self, user, password):
        restClient = restClientController(self.configFile.appTcpPort, self.trackerIP)
        userInfo = {}
        userInfo['user']=user
        userInfo['password']=password
        self.sessionToken = restClient.postLoginUser(userInfo)
        if (self.sessionToken != False):
            print(self.sessionToken)
            return True
        return False

    def register(self, user, password):
        restClient = restClientController(self.configFile.appTcpPort, self.trackerIP)
        userInfo = {}
        userInfo['user']=user
        userInfo['password']=password
        return restClient.postRegisterNewUser(userInfo)

    def shareResource (self, path):
        if (self.sessionToken!=False):
            fileController = FileManager()
            fileInfo = fileController.fileInfoScan(path)
            fileInfo['ip'] = self.configFile.localHostIP
            restClient = restClientController(self.configFile.appTcpPort, self.trackerIP)
            result = restClient.postAddNewResource(fileInfo, self.sessionToken)
            if (result!=False):
                cacheManager = cacheFilesManager(self.configFile.cachePathRoot, self.configFile.cachePathRoot)
                cacheManager.copyFileIntoChunks(result, path)
        return False

    def getResourceList (self):
        if (self.sessionToken!=False):
            restClient = restClientController(self.configFile.appTcpPort, self.trackerIP)
            return restClient.getRemoteResourceList(self.sessionToken)
        return False

    def downloadResource (self, uid):
        restClient = restClientController(self.configFile.appTcpPort, self.trackerIP)
        fileInfo = restClient.getRemoteResourceInfo(uid, self.sessionToken)
        if (fileInfo!=False):
            cacheManager = cacheFilesManager(self.configFile.cachePathRoot, self.configFile.cachePathRoot)
            useCaseRestClient = restClientController(self.configFile.appTcpPort, self.trackerIP)
            self.downloader = DownloadResource(cacheManager, useCaseRestClient)
            self.downloader.parameters(fileInfo['uid'], fileInfo['chunks'], fileInfo['host'], fileInfo['name'])
            self.downloader.execute(True)
            while (self.downloader.done != True):
                print ("Downloading: "+str(self.downloader.progress))
                time.sleep(0.5)
            return True
        return False

    def startServer (self):
        self.clientServer.startServer()




