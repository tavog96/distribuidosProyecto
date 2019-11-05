from ....lacus_common.core.common.interfaces.useCase import UseCase

class DownloadResource (UseCase):

    ###Parameters
    resourceUid = False
    resourceInfo = False

    def __init__(self):
        super(DownloadResource, self).__init__()

    def parameters(self, uid):
        self.resourceUid = uid
    
    def task(self):
        pass ## Use Case
    