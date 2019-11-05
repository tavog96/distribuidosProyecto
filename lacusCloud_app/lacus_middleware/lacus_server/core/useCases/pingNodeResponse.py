from ....lacus_common.core.common.interfaces.useCase import UseCase
from ..repositories.configFileController import configFileController

class PingNodeResponse (UseCase):

    ###Parameters
    nodeUid = False
    nodeIp = False
    configFile =  configFileController()

    def __init__(self, configController):
        super(PingNodeResponse, self).__init__()
        self.configFile = configController
        
    
    def task(self):
        self.configFile.scanConfigFile()
        self.response = self.configFile.localHostUid()
        self.setDone()
        
