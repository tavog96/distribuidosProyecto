from ...lacus_common.infrastructure.configFileController.configFileController import configFileController
from ...lacus_common.infrastructure.networkManagement.restClient import restClientController

def RegisterNode(trackerHostIP):
    configFile=configFileController()
    configFile.scanConfigFile()
    restClient = restClientController(configFile.appTcpPort, trackerHostIP)
    nodeInfo = {}
    nodeInfo['ip'] = configFile.localHostIP
    nodeInfo['uid'] = configFile.localHostUid
    result = restClient.postRegisterNewNode(nodeInfo)
    if (result!= False):
        return True
    return False