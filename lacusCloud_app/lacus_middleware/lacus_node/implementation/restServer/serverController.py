from....lacus_common.infrastructure.configFileController.configFileController import configFileController
from .restControllers.giveResourceChunk import GiveResourceChunk
from .restControllers.nodePing import NodePing
from .restControllers.uploadResourceOnNode import UploadResourceOnNode
from flask import Flask
from flask_restful import Api

class NodeController:

    app = Flask(__name__)
    api = Api(app)

    configFile = configFileController() 

    def __init__(self):
        super().__init__()
        self.configFile = configFileController()
        self.configFile.scanConfigFile()
        self.api.add_resource(NodePing, '/ping')
        self.api.add_resource(GiveResourceChunk, '/chunk/<string:uid>/<string:chunkNumber>')
        self.api.add_resource(UploadResourceOnNode, '/uploadResource')


    def startServer (self):
        self.app.run(port=self.configFile.appTcpPort)

