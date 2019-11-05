from ....lacus_common.core.common.interfaces.useCase import UseCase
from ..repositories.resourceDirectoryManagement import ResourceDirectoryManager


class GiveResourceList (UseCase):

    ###Parameters

    resourceManager = ResourceDirectoryManager()

    def __init__(self, resourceManager):
        super(GiveResourceList, self).__init__()
        self.resourceManager = resourceManager

    def parameters(self):
        return True
        
        
    
    def task(self):
        self.response =  self.resourceManager.getResourceList()
        self.setDone()
    