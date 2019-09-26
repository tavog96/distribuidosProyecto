from ....app_core.useCases.gelLocalResourceCacheInfo import getLocalResourceCacheInfo
from ....app_infrastructure.resourceManagement.resourceDirectoryManagement import resourceDirectoryManager
from ....app_infrastructure.cacheManagement.cacheDirectoryManagement import cacheDirectoryManager
from ....app_infrastructure.cacheManagement.cacheFilesManagement import cacheFilesManager
from ...common.configFileController import configFileController
from flask_restful import reqparse, abort, Resource
import json

class resourceController(Resource):

    configFile = configFileController()
    resourceDirManager = resourceDirectoryManager()
    cacheDirManager = cacheDirectoryManager(False)
    cacheFileManager = cacheFilesManager(False, False)
    useCase = getLocalResourceCacheInfo(False, False, False, False, False)

    def __init__(self):
        super().__init__()
        self.configFile.scanConfigFile()
        self.resourceDirManager = resourceDirectoryManager(self.configFile.resourceDirectoryFileName, configFileController.resourcePathRoot, False)
        self.cacheDirManager = cacheDirectoryManager(self.configFile.cacheDirectoryFileName)
        self.cacheFileManager = cacheFilesManager(self.configFile.cachePathRoot, self.configFile.resourcePathRoot)



    def get(self, uidParam):
        self.useCase = getLocalResourceCacheInfo(self.cacheDirManager, self.cacheFileManager, self.resourceDirManager, uidParam, configFileController.localHostIP)
        response = self.useCase.execute()
        if (response!=False):
            return response
        abort(500, message="Server can't proceed with this request")
