import requests
import json

class restClientController ():

    defaultPort = 50505
    remoteHostIP = ''

    def __init__(self, defaultPort, remoteHostIP):
        super().__init__()
        self.defaultPort = defaultPort
        self.remoteHostIP =  remoteHostIP
    
    # To connect to server
    def getRemoteResourceList (self, clientToken):
        raise NotImplementedError

    # To connect to server
    def getRemoteResourceInfo (self, uidParam, clientToken):
        raise NotImplementedError

    # To connect to server
    def postAddNewResource (self, fileInfo):
        raise NotImplementedError

    # To connect to node
    def postUploadNewResource (self, fileInfo):
        raise NotImplementedError

    # To connect to server
    def postRegisterNewNode  (self, nodeInfo):
        raise NotImplementedError

    # To connect to server
    def postRegisterNewUser  (self, UserInfo):
        raise NotImplementedError

    # To connect to server
    def postLoginUser  (self, UserInfo):
        raise NotImplementedError

    # To connect to node/client
    def getRemoteChunkFile (self, uidParam, chunkNumber):
        raise NotImplementedError

    # To connect to server
    def getVerificateToken (self, clientToken):
        raise NotImplementedError
    # To connect to node
    def getPingNode (self):
        raise NotImplementedError

    
    def transforTokenToTuples (self, token):
        raise NotImplementedError