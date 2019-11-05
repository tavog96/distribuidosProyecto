from .....lacus_common.core.useCases.streamResource import StreamResource
from .....lacus_common.infrastructure.cacheManagement.cacheFilesManagement import cacheFilesManager
from .....lacus_common.infrastructure.configFileController.configFileController import configFileController
from flask_restful import reqparse, abort, Resource
from flask import Flask
import json

class GiveResourceChunk(Resource):

    configFile = configFileController()
    cacheManager = cacheFilesManager(False, False)
    useCase = StreamResource(False)

    def __init__(self):
        super().__init__()
        self.cacheManager = cacheFilesManager(self.configFile.cachePathRoot, self.configFile.resourcePathRoot)
        self.useCase = StreamResource(self.cacheManager)

    def get(self, uid, chunkNumber):
        self.useCase.parameters(uid, int(chunkNumber))   
        self.useCase.execute()
        response = self.useCase.response
        if (response!=False):
            flaskApp = Flask(__name__)
            byteResponse = flaskApp.make_response(response)
            byteResponse.headers['content-type'] = 'application/octet-stream'
            return byteResponse
        abort(400, message="Resource not found")