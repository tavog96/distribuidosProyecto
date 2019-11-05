from....lacus_common.infrastructure.configFileController.configFileController import configFileController
from .restControllers.giveResourceListCon import GiveResourceListCon
from .restControllers.giveResourceInfoCon import GiveResourceInfoCon
from .restControllers.addResourceCon import AddResourceCon
from .restControllers.registerNodeCon import RegisterNodeCon
from .restControllers.authRegisterCon import AuthRegisterCon
from .restControllers.authLoginCon import AuthLoginCon
from flask import Flask
from flask_restful import Api

class serverController:

    app = Flask(__name__)
    api = Api(app)

    configFile = configFileController() 

    def __init__(self):
        super().__init__()
        self.configFile = configFileController()
        self.configFile.scanConfigFile()
        self.api.add_resource(GiveResourceListCon, '/resource')
        self.api.add_resource(GiveResourceInfoCon, '/resource/info/<string:uidParam>')
        self.api.add_resource(AddResourceCon, '/resource/add')
        self.api.add_resource(RegisterNodeCon, '/node/register')
        self.api.add_resource(AuthRegisterCon, '/user/register')
        self.api.add_resource(AuthLoginCon, '/user/login')


    def startServer (self):
        self.app.run(port=self.configFile.appTcpPort, host=self.configFile.localHostIP)

