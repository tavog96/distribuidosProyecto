import json, os.path

class jsonSaver:

    defaultFileName = ''

    def __init__(self, fileName = 'file.json'):
        super().__init__()
        self.defaultFileName = fileName
    
    def saveJson (self, inputObj):
        jsonSerializedObj = json.dumps(inputObj)
        file2save = open(self.defaultFileName, 'w')
        file2save.write(jsonSerializedObj)
        file2save.close()
    
    def openJson (self):
        if not os.path.exists(self.defaultFileName):
            return False
        file2read = open(self.defaultFileName,'r')
        fileRawContent = file2read.read()
        file2read.close()
        jsonDeserializedObj = json.loads(fileRawContent)
        return jsonDeserializedObj

