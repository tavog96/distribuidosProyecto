from ....lacus_common.infrastructure.jsonFileController.jsonSave import jsonSaver
from ....lacus_common.infrastructure.configFileController.configFileController import configFileController
import uuid



class UserDirectoryManager:
    directoryFileName="userDir.json"
    configController = configFileController ()
    jsonFile = jsonSaver()
    
    def __init__(self):
        self.configController.scanConfigFile()
        self.directoryFileName = self.configController.userDirectoryFileName
        self.jsonFile = jsonSaver(self.directoryFileName)

    def registerUser(self, username, password):
        rawDirectory = []
        rawDirectory = self.getAllUser()
        foundFlag = False
        for user in rawDirectory:
            if (user['username'] == username):
                foundFlag = True
                break
        if (not foundFlag):
            newUser = {}
            newUser['username'] = username
            newUser['password'] = password
            rawDirectory.append(newUser)
            self.jsonFile.saveJson(rawDirectory)
            return True
        return False
        
    def loginUser (self, username, password):
        rawDirectory = []
        rawDirectory = self.getAllUser()
        foundFlag = False
        for user in rawDirectory:
            if (user['username'] == username):
                if (user['password']== password):
                    token = str(uuid.uuid4())
                    user['session'] = token
                    self.jsonFile.saveJson(rawDirectory)
                    return token
                else:
                    return False
        return False

    def cerificateSession (self, key):
        rawDirectory = []
        rawDirectory = self.getAllUser()
        for user in rawDirectory:
            if ('session' in user):
                if (user['session']==key):
                    return True
        return False

  

    def getAllUser (self):
        rawDirectory = self.jsonFile.openJson()
        if (rawDirectory == False):
            self.createEmptyDirectory()
            rawDirectory = self.jsonFile.openJson()
        return rawDirectory

    def createEmptyDirectory (self):
        emptyContent = []
        self.jsonFile.saveJson(emptyContent)