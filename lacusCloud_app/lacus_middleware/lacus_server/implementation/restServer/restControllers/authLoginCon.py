from ....core.useCases.authLogin import AuthLogin
from ....infrastructure.userManagement.userDirectoryManagement import UserDirectoryManager
from flask_restful import reqparse, abort, Resource
from flask import Flask
import json

class AuthLoginCon(Resource):

    userManager = UserDirectoryManager()
    useCase = AuthLogin (False)
    parser = reqparse.RequestParser()
    parser.add_argument('user')
    parser.add_argument('password')

    def __init__(self):
        super().__init__()
        self.useCase = AuthLogin(self.userManager)


    def post(self):
        args = self.parser.parse_args()
        self.useCase.parameters(args['user'], args['password'])
        self.useCase.execute(False)
        if (self.useCase.response!=False):
            return json.dumps(self.useCase.response), 201
        abort(500, message="Server can't proceed with this request")
