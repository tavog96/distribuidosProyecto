
class configFileController:
    resourceDirectoryFileName = 'resourceDir.json'
    resourcePathRoot = './resources/'
    cacheDirectoryFileName = 'cacheDir.json'
    cachePathRoot = './cache/'
    localHostIP = '192.168.0.1'
    localHostUid = False
    appTcpPort = 55666
    nodeDirectoryFileName = 'nodeDir.json'
    userDirectoryFileName = 'userDir.json'

    def __init__(self):
        super().__init__()

    def scanConfigFile (self):
        raise NotImplementedError

    def setDefaultConfigFile (self):
        raise NotImplementedError