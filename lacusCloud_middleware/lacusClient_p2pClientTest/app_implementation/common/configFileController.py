from app_infrastructure.jsonFileController.jsonSave import jsonSaver

class configFileController:
    resourceDirectoryFileName = 'filesDir.json'
    resourcePathRoot = './files/'
    cacheDirectoryFileName = 'cacheDir.json'
    cachePathRoot = './cache/'
    localHostIP = '192.168.0.1'
    appTcpPort = 55666
    jsonController = jsonSaver('config.json')

    def __init__(self):
        super().__init__()

    def scanConfigFile (self):
        configFile = self.jsonController.openJson()
        if (configFile == False):
            self.setDefaultConfigFile()
            self.scanConfigFile()
        else:
            self.resourceDirectoryFileName = configFile['resourceDirectoryFileName']
            self.resourcePathRoot = configFile['resourcePathRoot']
            self.cacheDirectoryFileName = configFile['cacheDirectoryFileName']
            self.cachePathRoot = configFile['cachePathRoot']
            self.localHostIP = configFile['localHostIP']
            self.appTcpPort = configFile['appTcpPort']
            return configFile

    def setDefaultConfigFile (self):
        configContent = {}
        configContent['resourceDirectoryFileName'] = self.resourceDirectoryFileName
        configContent['resourcePathRoot'] = self.resourcePathRoot
        configContent['cacheDirectoryFileName'] = self.cacheDirectoryFileName
        configContent['cachePathRoot'] =  self.cachePathRoot
        configContent['localHostIP'] =  self.localHostIP
        configContent['appTcpPort'] = self.appTcpPort
        self.jsonController.saveJson(configContent)