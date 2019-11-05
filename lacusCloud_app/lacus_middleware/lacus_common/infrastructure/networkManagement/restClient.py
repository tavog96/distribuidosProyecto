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
        url = "http://"+self.remoteHostIP+':'+str(self.defaultPort)+'/resource'
        try:
            response = requests.get(url, params=self.transforTokenToTuples(clientToken))
            if response.ok:
                responseContent = json.loads(response.content)
                return responseContent
            return False
        except:
            return False

    # To connect to server
    def getRemoteResourceInfo (self, uidParam, clientToken):
        url = "http://"+self.remoteHostIP+':'+str(self.defaultPort)+'/resource/info/'+uidParam
        try:
            response = requests.get(url, params=self.transforTokenToTuples(clientToken))
            if response.ok:
                responseContent = json.loads(json.loads(response.content))
                return responseContent
            return False
        except:
            return False

    # To connect to server
    def postAddNewResource (self, fileInfo, token):
        url = "http://"+self.remoteHostIP+':'+str(self.defaultPort)+'/resource/add'
        try:
            response = requests.post(url, data=fileInfo, params=self.transforTokenToTuples(token))
            if response.ok:
                responseContent = json.loads(json.loads(response.content))
                return responseContent
            return False
        except:
            return False

    # To connect to node
    def postUploadNewResource (self, fileInfo, remoteHost):
        host = []
        host.append(remoteHost)
        fileInfo['host'] = json.dumps(host)
        try:
            url = "http://"+self.remoteHostIP+':'+str(self.defaultPort)+'/uploadResource'
            response = requests.post(url, data=fileInfo, timeout = 1)
            if response.ok:
                return True
            return False
        except:
            return False

    # To connect to server
    def postRegisterNewNode  (self, nodeInfo):
        url = "http://"+self.remoteHostIP+':'+str(self.defaultPort)+'/node/register'
        try:
            response = requests.post(url, data=nodeInfo, timeout = 2)
            if response.ok:
                responseContent = json.loads(response.content)
                return responseContent
            return False
        except:
            return False

    # To connect to server
    def postRegisterNewUser  (self, UserInfo):
        url = "http://"+self.remoteHostIP+':'+str(self.defaultPort)+'/user/register'
        try:
            response = requests.post(url, data=UserInfo)
            if response.ok:
                responseContent = json.loads(response.content)
                return responseContent
            return False
        except:
            return False

    # To connect to server
    def postLoginUser  (self, UserInfo):
        url = "http://"+self.remoteHostIP+':'+str(self.defaultPort)+'/user/login'
        try:
            response = requests.post(url, data=UserInfo)
            if response.ok:
                responseContent = json.loads(json.loads(response.content))
                return responseContent
            return False
        except:
            return False

    # To connect to node/client
    def getRemoteChunkFile (self, uidParam, chunkNumber):
        url = "http://"+self.remoteHostIP+':'+str(self.defaultPort)+'/chunk/'+uidParam+'/'+str(chunkNumber)
        try:
            response = requests.get(url, timeout = 1)
            if response.ok:
                return response.content
            return False
        except:
            return False

    # To connect to server
    def getVerificateToken (self, clientToken):
        url = "http://"+self.remoteHostIP+':'+str(self.defaultPort)+'/token'
        try:
            response = requests.get(url, params=self.transforTokenToTuples(clientToken))
            if response.ok:
                return json.loads(response.content)
            return False
        except:
            return False

    # To connect to node
    def getPingNode (self):
        url = "http://"+self.remoteHostIP+':'+str(self.defaultPort)+'/ping'
        try:
            response = requests.get(url, timeout = 0.5)
            if response.ok:
                return json.loads(response.content)
            return False
        except:
            return False

    
    def transforTokenToTuples (self, token):
        param = {}
        param['token'] = token
        return param