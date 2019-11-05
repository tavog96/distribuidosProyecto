from ....lacus_common.core.common.interfaces.useCase import UseCase

class ShareResource (UseCase):

    ###Parameters
    resourcePath = False
    resourceName = False
    resourceSize =  0
    resourceLastModificate = 0

    def __init__(self):
        super(ShareResource, self).__init__()

    def parameters(self, path, name, size, lastMotificate):
        self.resourcePath = path
        self.resourceName = name
        self.resourceSize = size
        self.resourceLastModificate = lastMotificate
    
    def task(self):
        pass ## Use Case
    