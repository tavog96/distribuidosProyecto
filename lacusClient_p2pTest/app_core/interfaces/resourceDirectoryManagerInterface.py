class resourceDirectoryManagerInterface:

    def __init__(self, directoryFileName = 'filesDir.json', directoryRootPath = './files', versionControl= False):
        super().__init__()


    def scanDirectory(self):
        raise NotImplementedError()

    def getResourceInfo (self, fileName = False, fileUID = False):
        raise NotImplementedError()

    def getResourcesInfo (self):
        raise NotImplementedError()

