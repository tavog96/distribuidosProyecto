from ....lacus_common.infrastructure.jsonFileController.jsonSave import jsonSaver
from ....lacus_common.infrastructure.configFileController.configFileController import configFileController

class NodeDirectoryManager:

    directoryFileName="nodeDir.json"
    configController = configFileController ()
    jsonFile = jsonSaver()

    def __init__(self):
        self.configController.scanConfigFile()
        self.directoryFileName = self.configController.nodeDirectoryFileName
        self.jsonFile = jsonSaver(self.directoryFileName)

    def updateNode(self, hostIp, hostUid):
        rawDirectory = []
        rawDirectory = self.getAllNodes()
        foundFlag = False
        for node in rawDirectory:
            if (node['uid'] == hostUid):
                node['ip'] = hostIp
                foundFlag = True
                break
        if (not foundFlag):
            newNode = {}
            newNode['uid'] = hostUid
            newNode['ip'] = hostIp
            rawDirectory.append(newNode)
        self.jsonFile.saveJson(rawDirectory)
        return True
        

    def getNodeIp (self, hostUid):
        rawDirectory = []
        rawDirectory = self.getAllNodes()
        for node in rawDirectory:
            if (node['uid'] == hostUid):
                return node['ip']
        return False


    def removeNode (self, hostUid):
        itemToDelete = False
        rawDirectory = []
        rawDirectory = self.getAllNodes()
        for node in rawDirectory:
            if (node['uid']==hostUid):
                itemToDelete = node
                break
        if (itemToDelete != False):
            rawDirectory.remove(itemToDelete)
            self.jsonFile.saveJson(rawDirectory)
            return True
        return False


    def getAllNodes (self):
        rawDirectory = self.jsonFile.openJson()
        if (rawDirectory == False):
            self.createEmptyDirectory()
            rawDirectory = self.jsonFile.openJson()
        return rawDirectory


    def createEmptyDirectory (self):
        emptyContent = []
        self.jsonFile.saveJson(emptyContent)




