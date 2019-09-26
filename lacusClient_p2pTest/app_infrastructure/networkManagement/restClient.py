from ...app_core.interfaces.restClientControllerInterface import restClientControllerInterface
import requests
import json

class restClientController (restClientControllerInterface):

    defaultPort = 50505
    remoteHostIP = ''

    def __init__(self, defaultPort, remoteHostIP):
        super().__init__()
        self.defaultPort = defaultPort
        self.remoteHostIP =  remoteHostIP
    
    def getRemoteResourceList (self):
        url = "http://"+self.remoteHostIP+':'+str(self.defaultPort)+'/resource'
        response = requests.get(url)
        if response.ok:
            responseContent = json.loads(response.content)
            return responseContent
        return False

    def getRemoteResourceCacheInfo (self, uidParam):
        url = "http://"+self.remoteHostIP+':'+str(self.defaultPort)+'/resource/'+uidParam
        response = requests.get(url)
        if response.ok:
            responseContent = json.loads(response.content)
            return responseContent
        return False


    def getRemoteChunkFile (self, uidParam, chunkNumber):
        url = "http://"+self.remoteHostIP+':'+str(self.defaultPort)+'/chunk/'+uidParam+'/'+str(chunkNumber)
        response = requests.get(url)
        if response.ok:
            return response.content
        return False