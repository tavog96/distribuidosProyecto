from ....app_core.useCases.getLocalResourceChunk import getLocalResourceChunk
from ....app_infrastructure.cacheManagement.cacheFilesManagement import cacheFilesManager
from ....app_infrastructure.cacheManagement.cacheDirectoryManagement import cacheDirectoryManager
from ...common.configFileController import configFileController
from flask_restful import reqparse, abort, Resource
from flask import Flask

class chunkFileController(Resource):

    configFile = configFileController()
    cacheFileManager = cacheFilesManager(False,False)
    cacheDirManager = cacheDirectoryManager(False)
    useCase = getLocalResourceChunk(False, False, False, False)

    def __init__(self):
        super().__init__()
        self.configFile.scanConfigFile()
        self.cacheDirManager = cacheDirectoryManager(self.configFile.cacheDirectoryFileName)
        self.cacheFileManager = cacheFilesManager(self.configFile.cachePathRoot, self.configFile.resourcePathRoot)

    def get(self, uidParam, chunkNumber):
        chunkNumberParam = False
        try:
            chunkNumberParam = int(chunkNumber)
        except:
            abort(400, message="A correct numeric Chunk index must be provided")
            return
        if (chunkNumberParam != False):
            self.useCase = getLocalResourceChunk(self.cacheDirManager, self.cacheFileManager, uidParam, chunkNumberParam)
            response = self.useCase.execute()
            if (response!=False):
                flaskApp = Flask(__name__)
                byteResponse = flaskApp.make_response(response)
                byteResponse.headers['content-type'] = 'application/octet-stream'
                return byteResponse
        ### Look here for ChunkFile bianry content
        abort(404, message="File not found on this server")