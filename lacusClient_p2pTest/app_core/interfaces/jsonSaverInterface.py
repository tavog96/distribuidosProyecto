class jsonSaverInterface:

    def __init__(self, fileName = 'file.json'):
        super().__init__()
    
    def saveJson (self, inputObj):
        raise NotImplementedError()
    
    def openJson (self):
        raise NotImplementedError()