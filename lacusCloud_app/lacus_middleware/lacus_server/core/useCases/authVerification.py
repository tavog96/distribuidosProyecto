from ....lacus_common.core.common.interfaces.useCase import UseCase
from ...core.repositories.userDirectoryManagement import UserDirectoryManager

class AuthVerification (UseCase):

    ###Parameters
    hostToken = False

    userManager = UserDirectoryManager()

    def __init__(self, userManager):
        super(AuthVerification, self).__init__()
        self.userManager  = userManager

    def parameters(self, token):
        self.hostToken = token      
        
        
    def task(self):
        self.response = self.userManager.cerificateSession(self.hostToken)
        self.setDone()
    