from .resourceVersionControl import versionController

class integrityMonitor:

    dirVersionController = versionController()

    def __init__(self, versionControl=False):
        super().__init__()
        self.dirVersionController = versionController(versionControl) 

    def integrityVerification (self, savedDirectory, scannedDirectory):
        if savedDirectory == False:
            return self.dirVersionController.firstVersionGenerator(scannedDirectory)
        resultDirectory = []
        for scannedFileInfo in scannedDirectory:
            scannedFileInfo = self.dirVersionController.setDefaultAsNewFile(scannedFileInfo)
            flagAlreadySavedFile = False
            for savedFileInfo in savedDirectory:
                if scannedFileInfo['name']== savedFileInfo['name']:
                    flagAlreadySavedFile = True
                    scannedFileInfo = self.dirVersionController.determinateLastVersion(scannedFileInfo, savedFileInfo)
                    break
                if (not flagAlreadySavedFile):
                    scannedFileInfo = self.dirVersionController.setNewUID(scannedFileInfo)
            resultDirectory.append(scannedFileInfo)
        return resultDirectory