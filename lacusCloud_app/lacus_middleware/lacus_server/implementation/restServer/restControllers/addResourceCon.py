from ....core.useCases.addResource import AddResource
from .....lacus_common.infrastructure.networkManagement.restClient import  restClientController
from ....infrastructure.nodeMangement.nodeDirectoryManagement import NodeDirectoryManager
from ....infrastructure.resourceManagement.resourceDirectoryManagement import ResourceDirectoryManager
from .....lacus_common.infrastructure.configFileController.configFileController import configFileController
from ....infrastructure.userManagement.userDirectoryManagement import UserDirectoryManager
from ....core.useCases.authVerification import AuthVerification
from flask_restful import reqparse, abort, Resource
from flask import Flask
import json

class AddResourceCon(Resource):

    authUseCase = AuthVerification(False)
    userManager = UserDirectoryManager()

    configController = configFileController()
    nodeManager = NodeDirectoryManager()
    resourceManager = ResourceDirectoryManager()
    restController = restClientController(False, False)
    useCase = AddResource (False, False, False)
    parser = reqparse.RequestParser()
    #name, size, lastmodificate, ip
    parser.add_argument('name')
    parser.add_argument('size')
    parser.add_argument('lastmodificate')
    parser.add_argument('ip')
    parser.add_argument('token')

    def __init__(self):
        super().__init__()
        self.configController.scanConfigFile()
        self.restController = restClientController(self.configController.appTcpPort, False)
        self.useCase = AddResource(self.resourceManager, self.restController, self.nodeManager)
        self.authUseCase = AuthVerification(self.userManager)

    def post(self):
        args = self.parser.parse_args()
        if (args['token'] != None):
            self.authUseCase.parameters(args['token'])
            self.authUseCase.execute()
            if (self.authUseCase.response):

                self.useCase.parameters(args['name'], float(args['size']), float(args['lastmodificate']), args['ip'])
                self.useCase.execute(False)
                if (self.useCase.response != False):
                    return json.dumps(self.useCase.response), 201
                abort(500, message="Server can't proceed with this request")
            
        abort(401, message="Not authorized user's token provided")
