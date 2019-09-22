import uuid

class versionController:

    activate = True

    def __init__(self, activationSwitcher = True):
        super().__init__()
        self.activate = activationSwitcher

    def filePropertiesNewVersionChecker (self, savedFileProps, scannedFileProps):
        if (savedFileProps['size']!=scannedFileProps['size']):
            return True
        if (savedFileProps['lastmodificate']!=scannedFileProps['lastmodificate']):
            return True
        return False

    def firstVersionGenerator (self, originDirectory):
        for fileInfo in originDirectory:
            fileInfo['uid'] = str(uuid.uuid1())
            if (self.activate):
                fileInfo['version']=1
        return originDirectory

    def setDefaultAsNewFile (self, scannedFile):
        if self.activate:
            scannedFile['version'] = 1
        return scannedFile

    def setNewUID (self, scannedFile):
        scannedFile['uid']=str(uuid.uuid1)
        return scannedFile

    def determinateLastVersion (self, scannedFileInfo, savedFileInfo):
        if self.filePropertiesNewVersionChecker(savedFileInfo, scannedFileInfo):## True if there are modifications
            if (self.activate):
                scannedFileInfo['version']=(savedFileInfo['version']+1) ## Setting new version
                scannedFileInfo['uid'] = savedFileInfo['uid']  ## keeping the same UDI
            else:
                scannedFileInfo['uid'] = str(uuid.uuid1()) ## If there is not version control, just create a new UID
        else:
            if (self.activate):
                scannedFileInfo['version']=savedFileInfo['version']
            scannedFileInfo['uid'] = savedFileInfo['uid']
        return scannedFileInfo
