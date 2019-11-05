from ....core.useCases.giveResourceList import GiveResourceList
from ....infrastructure.resourceManagement.resourceDirectoryManagement import ResourceDirectoryManager
from ....core.useCases.authVerification import AuthVerification
from ....infrastructure.userManagement.userDirectoryManagement import UserDirectoryManager
from flask_restful import reqparse, abort, Resource
import json

class GiveResourceListCon(Resource):

    authUseCase = AuthVerification(False)
    userManager = UserDirectoryManager()

    resourceDirManager = ResourceDirectoryManager()
    useCase = GiveResourceList(resourceDirManager)
    parser = reqparse.RequestParser()
    parser.add_argument('token') 

    def __init__(self):
        super().__init__()
        self.useCase = GiveResourceList(self.resourceDirManager)
        self.authUseCase = AuthVerification(self.userManager)

    def get(self):
        args = self.parser.parse_args()
        if (args['token'] != None):
            self.authUseCase.parameters(args['token'])
            self.authUseCase.execute()
            if (self.authUseCase.response):
                
                self.useCase.execute()
                response = self.useCase.response
                if (response!=False):
                    return json.dumps(response)
                abort(500, message="Server can't proceed with this request")

        abort(401, message="Not authorized user's token provided")