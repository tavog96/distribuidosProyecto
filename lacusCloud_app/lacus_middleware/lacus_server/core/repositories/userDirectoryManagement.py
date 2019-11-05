

class UserDirectoryManager:


    def registerUser(self, username, password):
        raise NotImplementedError
        
    def loginUser (self, username, password):
        raise NotImplementedError
                

    def getAllUser (self):
        raise NotImplementedError

    def createEmptyDirectory (self):
        raise NotImplementedError

    def cerificateSession (self, key):
        raise NotImplementedError