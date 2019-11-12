from ..common.interfaces.service import Service
from ...infrastructure.nodeMangement.nodeDirectoryManagement import NodeDirectoryManager
from ....lacus_common.infrastructure.networkManagement.restClient import restClientController
from ....lacus_common.infrastructure.configFileController.configFileController import configFileController
from ...core.useCases.pingNode import pingNode
import json


class PingNodeService(Service):

    nodeManager = NodeDirectoryManager()
    configFile = configFileController()

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.timeWait = 1
        self.nodeManager = NodeDirectoryManager()

    def task(self):
        nodes = self.nodeManager.getAllNodes()
        nodes2delete = []
        for node in nodes:
            restController = restClientController(self.configFile.appTcpPort, node['ip'])
            print('sending ping to '+  node['ip'])
            useCase = pingNode(restController)
            useCase.execute(asynchronousParam=False)
            response = useCase.response
            if (response!=False):
                self.nodeManager.updateNode(node['ip'], response)
            else:
                nodes2delete.append(node)
        for deletable in nodes2delete:
            self.nodeManager.removeNode(deletable['uid'])
    

        

