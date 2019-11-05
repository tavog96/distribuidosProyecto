from ....lacus_common.infrastructure.configFileController.configFileController import configFileController
from .restControllers.giveResourceChunk import GiveResourceChunk
from flask import Flask
from flask_restful import Api

class ClientController:

    app = Flask(__name__)
    api = Api(app)

    configFile = configFileController() 

    def __init__(self):
        super().__init__()
        self.configFile = configFileController()
        self.configFile.scanConfigFile()
        self.api.add_resource(GiveResourceChunk, '/chunk/<string:uid>/<string:chunkNumber>')


    def startServer (self):
        self.configFile.scanConfigFile()
        self.app.run(port=self.configFile.appTcpPort, debug=False, host=self.configFile.localHostIP)

