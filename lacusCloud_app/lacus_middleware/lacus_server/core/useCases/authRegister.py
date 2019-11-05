from ....lacus_common.core.common.interfaces.useCase import UseCase
from ...core.repositories.userDirectoryManagement import UserDirectoryManager

class AuthRegister (UseCase):

    ###Parameters
    hostUser = False
    hostPassword = False

    userManager = UserDirectoryManager()

    def __init__(self, userDirectoryManager):
        super(AuthRegister, self).__init__()
        self.userManager = userDirectoryManager

    def parameters(self, user, password):
        self.hostUser = user
        self.hostPassword = password
        
    
    def task(self):
        if (self.hostUser != False and self.hostPassword!= False):
            self.response = self.userManager.registerUser(self.hostUser, self.hostPassword)
            self.setDone()
            return
        self.response = False
        self.setDone()
    