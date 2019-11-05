from ....lacus_common.core.common.interfaces.useCase import UseCase
from ...core.repositories.userDirectoryManagement import UserDirectoryManager

class AuthLogin (UseCase):

    ###Parameters
    hostUser = False
    hostPassword = False

    userManager = UserDirectoryManager()

    def __init__(self, userDirectoryManager):
        super(AuthLogin, self).__init__()
        self.userManager=userDirectoryManager

    def parameters(self, user, password):
        self.hostPassword = password
        self.hostUser =user
        
    
    def task(self):
        if (self.hostUser != False and self.hostPassword!= False):
            token = self.userManager.loginUser(self.hostUser, self.hostPassword)
            self.response = token
            self.setDone()
            return
        self.response = False
        self.setDone()
    