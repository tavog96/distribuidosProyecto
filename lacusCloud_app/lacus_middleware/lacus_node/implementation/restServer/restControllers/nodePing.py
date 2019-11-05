from .....lacus_common.infrastructure.configFileController.configFileController import configFileController
from flask_restful import reqparse, abort, Resource
import json

class NodePing(Resource):

    controlFile = configFileController()


    def __init__(self):
        super().__init__()
        self.controlFile.scanConfigFile()
        


    def get(self):
        response = self.controlFile.localHostUid
        if (response!=False):
            return json.dumps(response)
        abort(500, message="Server unable to handle this request")
