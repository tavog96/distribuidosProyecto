from ....core.useCases.registerNode import RegisterNode
from .....lacus_common.infrastructure.networkManagement.restClient import  restClientController
from ....infrastructure.nodeMangement.nodeDirectoryManagement import NodeDirectoryManager
from ....infrastructure.resourceManagement.resourceDirectoryManagement import ResourceDirectoryManager
from .....lacus_common.infrastructure.configFileController.configFileController import configFileController
from flask_restful import reqparse, abort, Resource
from flask import Flask
import json

class RegisterNodeCon(Resource):

    nodeManager = NodeDirectoryManager()
    useCase = RegisterNode (False)
    parser = reqparse.RequestParser()
    parser.add_argument('uid')
    parser.add_argument('ip')

    def __init__(self):
        super().__init__()
        self.useCase = RegisterNode(self.nodeManager)

    def post(self):
        args = self.parser.parse_args()
        self.useCase.parameters(args['uid'], args['ip'])
        self.useCase.execute(False)
        if (self.useCase.response!=False):
            return json.dumps(self.useCase.response), 201
        abort(500, message="Server can't proceed with this request")
