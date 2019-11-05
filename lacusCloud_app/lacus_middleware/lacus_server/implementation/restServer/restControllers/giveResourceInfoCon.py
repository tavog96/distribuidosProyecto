from ....core.useCases.giveResourceInfo import GiveResourceInfo
from ....infrastructure.resourceManagement.resourceDirectoryManagement import ResourceDirectoryManager
from ....infrastructure.nodeMangement.nodeDirectoryManagement import NodeDirectoryManager
from ....infrastructure.userManagement.userDirectoryManagement import UserDirectoryManager
from ....core.useCases.authVerification import AuthVerification
from flask_restful import reqparse, abort, Resource
import json

class GiveResourceInfoCon(Resource):

    authUseCase = AuthVerification(False)
    userManager = UserDirectoryManager()

    resourceManager = ResourceDirectoryManager()
    nodeManager= NodeDirectoryManager()
    useCase = GiveResourceInfo(False, False)
    parser = reqparse.RequestParser()
    parser.add_argument('token')  

    def __init__(self):
        super().__init__()
        self.useCase = GiveResourceInfo(self.resourceManager, self.nodeManager)
        self.authUseCase = AuthVerification(self.userManager)


    def get(self, uidParam):
        args = self.parser.parse_args()
        if (args['token'] != None):
            self.authUseCase.parameters(args['token'])
            self.authUseCase.execute()
            if (self.authUseCase.response):

                self.useCase.parameters(uidParam)
                self.useCase.execute()
                response = self.useCase.response
                if (response!=False):
                    return json.dumps(response)
                abort(400, message="Resource not found in server")
        
        abort(401, message="Not authorized user's token provided")
