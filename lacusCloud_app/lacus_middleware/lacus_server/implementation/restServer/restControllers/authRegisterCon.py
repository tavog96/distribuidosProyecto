from ....core.useCases.authRegister import AuthRegister
from ....infrastructure.userManagement.userDirectoryManagement import UserDirectoryManager
from flask_restful import reqparse, abort, Resource
from flask import Flask
import json

class AuthRegisterCon(Resource):

    userManager = UserDirectoryManager()
    useCase = AuthRegister(False)
    parser = reqparse.RequestParser()
    parser.add_argument('user')
    parser.add_argument('password')

    def __init__(self):
        super().__init__()
        self.useCase = AuthRegister(self.userManager)

    def post(self):
        args = self.parser.parse_args()
        self.useCase.parameters(args['user'],args['password'])
        self.useCase.execute(False)
        if (self.useCase.response!=False):
            return json.dumps(self.useCase.response), 201
        abort(500, message="Server can't proceed with this request")
