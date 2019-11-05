from .....lacus_common.infrastructure.networkManagement.restClient import  restClientController
from .....lacus_common.infrastructure.cacheManagement.cacheFilesManagement import cacheFilesManager
from .....lacus_common.infrastructure.configFileController.configFileController import configFileController
from .....lacus_common.core.useCases.downloadResource import DownloadResource
from flask_restful import reqparse, abort, Resource
from flask import Flask
import json

class UploadResourceOnNode(Resource):

    configFile = configFileController ()
    cacheManager = cacheFilesManager(False, False)
    restController = restClientController (False, False)
    useCase = DownloadResource (False, False)
    parser = reqparse.RequestParser()
    parser.add_argument('uid')
    parser.add_argument('name')
    parser.add_argument('size')
    parser.add_argument('lastmodificate')
    parser.add_argument('chunks')
    parser.add_argument('uploadDate')
    parser.add_argument('chunkSize')
    parser.add_argument('host')
    

    def __init__(self):
        super().__init__()
        self.configFile.scanConfigFile()
        self.cacheManager = cacheFilesManager(self.configFile.cachePathRoot, self.configFile.resourcePathRoot)
        self.restController = restClientController(self.configFile.appTcpPort, self.configFile.localHostIP)
        self.useCase = DownloadResource(self.cacheManager, self.restController)

    def post(self):
        args = self.parser.parse_args()
        self.useCase.parameters(args['uid'], int(args['chunks']), json.loads(args['host']))
        self.useCase.execute(True)
        return json.dumps(True), 201
