from .restControllers.chunkFileController import chunkFileController
from .restControllers.resourceController import resourceController
from .restControllers.resourcesListController import resourcesListController

from flask import Flask
from flask_restful import Api

class serverController:

    app = Flask(__name__)
    api = Api(app)

    configFile ={} 

    def __init__(self, configFileParam):
        super().__init__()
        self.api.add_resource(resourcesListController, '/resource')
        self.api.add_resource(resourceController, '/resource/<string:uidParam>')
        self.api.add_resource(chunkFileController, '/chunk/<string:uidParam>/<string:chunkNumber>')
        self.configFile = configFileParam

    def startServer (self):
        self.app.run(port=self.configFile['appTcpPort'])

