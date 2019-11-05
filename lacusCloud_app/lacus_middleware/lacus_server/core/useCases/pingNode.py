from ....lacus_common.core.common.interfaces.useCase import UseCase
from ..repositories.restClient import restClientController

class pingNode (UseCase):

    ###Parameters

    restController = restClientController(False, False)

    def __init__(self, restController):
        super(pingNode, self).__init__()
        self.restController = restController
        

    def parameters(self):
        return False
        
    
    def task(self):
        self.response = self.restController.getPingNode()
        self.setDone()


    