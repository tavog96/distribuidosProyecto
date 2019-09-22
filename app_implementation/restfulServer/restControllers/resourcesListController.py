from app_core.useCases.getLocalResourceList import getLocalResourceList
from app_infrastructure.resourceManagement.resourceDirectoryManagement import resourceDirectoryManager
from ...common.configFileController import configFileController
from flask_restful import reqparse, abort, Resource
import json

class resourcesListController(Resource):

    configFile = configFileController()
    resourceDirManager = resourceDirectoryManager()
    useCase = getLocalResourceList(resourceDirManager)

    def __init__(self):
        super().__init__()
        self.configFile.scanConfigFile()
        self.resourceDirManager = resourceDirectoryManager(self.configFile.resourceDirectoryFileName, configFileController.resourcePathRoot, False)
        self.useCase = getLocalResourceList(self.resourceDirManager)

    def get(self):
        response = self.useCase.execute()
        if (response!=False):
            return json.dumps(response)
        abort(500, message="Server can't proceed with this request")