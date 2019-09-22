from app_implementation.restfulServer.serverController import serverController
from app_implementation.common.configFileController import configFileController
from app_infrastructure.resourceManagement.resourceDirectoryManagement import resourceDirectoryManager

configFile = configFileController()
configSettings = configFile.scanConfigFile()
resourceDirManager = resourceDirectoryManager (configFile.resourceDirectoryFileName, configFile.resourcePathRoot, False)
resourceDirManager.scanDirectory()


server = serverController(configSettings)

server.startServer()