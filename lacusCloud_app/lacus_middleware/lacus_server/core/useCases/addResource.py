from ....lacus_common.core.common.interfaces.useCase import UseCase
from ...core.repositories.resourceDirectoryManagement import ResourceDirectoryManager
from ...core.repositories.restClient import restClientController
from ...core.repositories.nodeDirectoryManagement import NodeDirectoryManager
from threading import Thread
import random

class AddResource (UseCase):

    ###Parameters
    resourceName = False
    resourceSize = 0
    resourceLastModificate = 0
    resourceIp = False
    resourceManager = ResourceDirectoryManager()
    nodeManager = NodeDirectoryManager()
    restController = restClientController (False, False)
    uploadRequestThread = False

    def __init__(self, resourceManager, restController, nodeManager):
        super(AddResource, self).__init__()
        self.resourceManager = resourceManager
        self.restController = restController
        self.nodeManager = nodeManager


    def parameters(self, name, size, lastModificate, Ip):
        self.resourceIp = Ip
        self.resourceName = name
        self.resourceSize = size
        self.resourceLastModificate = lastModificate
        
    
    def task(self):
        fileInfo = {}
        fileInfo['name']= self.resourceName
        fileInfo['size'] = self.resourceSize
        fileInfo['lastmodificate'] = self.resourceLastModificate
        resultFileInfo = self.resourceManager.addResource(fileInfo)
        self.response = resultFileInfo
        self.setDone()
        if (resultFileInfo != False):
            self.uploadRequestThread = Thread(target=self.sendUploadRequest)
            self.uploadRequestThread.start()


    def sendUploadRequest (self):
        #CREATE UPLOAD COMMAND FOR NODES
        nodes = self.nodeManager.getAllNodes()
        allnodecounter = len(nodes)
        if (len(nodes)>0):
            selectedNode =  random.randint(0,(len(nodes)-1))
            nodeCounter = 0
            responseCopy = {}
            responseCopy['name'] = self.response['name']
            responseCopy['size'] = self.response['size']
            responseCopy['lastmodificate'] = self.response['lastmodificate']
            responseCopy['uid'] = self.response['uid']
            responseCopy['chunks'] = self.response['chunks']
            responseCopy['chunkSize'] = self.response['chunkSize']
            responseCopy['uploadDate'] = self.response['uploadDate']

            while (nodeCounter<len(nodes)):
                remoteHost = ""
                if (selectedNode == nodeCounter):
                    remoteHost = self.resourceIp
                else:
                    remoteHost = nodes[selectedNode]['ip']
                self.restController.remoteHostIP = nodes[nodeCounter]['ip']
                if (self.restController.postUploadNewResource(responseCopy, remoteHost)):
                    self.resourceManager.addHostToResource(responseCopy['uid'], nodes[nodeCounter]['uid'])
                nodeCounter=nodeCounter+1

        
    