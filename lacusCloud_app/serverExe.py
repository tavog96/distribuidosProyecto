from lacus_middleware.lacus_server.implementation.restServer.serverController import serverController
from lacus_middleware.lacus_common.infrastructure.configFileController.configFileController import configFileController
from lacus_middleware.lacus_server.implementation.services.pingNodeService import PingNodeService
from lacus_middleware.lacus_node.implementation.restServer.serverController import NodeController
from lacus_middleware.lacus_node.implementation.registerNode import RegisterNode
from threading import Thread
import time

def startServer():
    pingService = PingNodeService()
    pingService.start(1)
    server = serverController()
    server.startServer()

def startNode():
    node = NodeController()
    node.startServer()


configFile = configFileController()
configFile.scanConfigFile()
if (configFile.serverMode == 'tracker'):
    startServer()
if (configFile.serverMode == 'node'):
    threadNode = Thread(target=startNode)
    threadNode.start()
    flagConneted = False
    time.sleep(2)
    while (not flagConneted):
        trackerIP = input('Set the tracker host IP: ')
        if (RegisterNode(trackerIP)==True):
            flagConneted = True
        else:
            print('Unable to connect to tracker')
print ('Go check config.json on the app path, and update serverMode and localHostIP to the current values')

