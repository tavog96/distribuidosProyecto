from ...infrastructure.jsonFileController.jsonSave import jsonSaver
import uuid

class configFileController:
    resourceDirectoryFileName = 'resourceDir.json'
    resourcePathRoot = './downloads/'
    cacheDirectoryFileName = 'cacheDir.json'
    cachePathRoot = './cache/'
    localHostIP = '192.168.0.1'
    localHostUid = False
    appTcpPort = 55666
    nodeDirectoryFileName = 'nodeDir.json'
    userDirectoryFileName = 'userDir.json'
    jsonController = jsonSaver('config.json')
    serverMode = 'none'

    def __init__(self):
        super().__init__()

    def scanConfigFile (self):
        configFile = self.jsonController.openJson()
        if (configFile == False):
            self.setDefaultConfigFile()
            configFile = self.jsonController.openJson()
        else:
            self.resourceDirectoryFileName = configFile['resourceDirectoryFileName']
            self.resourcePathRoot = configFile['downloadsPathRoot']
            self.cacheDirectoryFileName = configFile['cacheDirectoryFileName']
            self.cachePathRoot = configFile['cachePathRoot']
            self.localHostIP = configFile['localHostIP']
            self.appTcpPort = configFile['appTcpPort']
            self.localHostUid = configFile['localHostUid']
            self.nodeDirectoryFileName = configFile['nodeDirectoryFileName']
            self.userDirectoryFileName = configFile['userDirectoryFileName']
            self.serverMode = configFile['serverMode']
            
            return configFile

    def setDefaultConfigFile (self):
        configContent = {}
        configContent['resourceDirectoryFileName'] = self.resourceDirectoryFileName
        configContent['downloadsPathRoot'] = self.resourcePathRoot
        configContent['cacheDirectoryFileName'] = self.cacheDirectoryFileName
        configContent['cachePathRoot'] =  self.cachePathRoot
        configContent['localHostIP'] =  self.localHostIP
        configContent['appTcpPort'] = self.appTcpPort
        configContent['localHostUid'] = str(uuid.uuid1())
        configContent['nodeDirectoryFileName'] = self.nodeDirectoryFileName
        configContent['userDirectoryFileName'] = self.userDirectoryFileName
        configContent['serverMode'] = self.serverMode
        self.jsonController.saveJson(configContent)

    def fileExist (self):
        file = self.jsonController.openJson()
        if (file !=False):
            return True
        return False