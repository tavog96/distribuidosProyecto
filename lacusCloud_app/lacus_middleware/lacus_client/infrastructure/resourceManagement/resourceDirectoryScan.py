import os

class filesScaner:

    defaultAppPath = ''

    def __init__(self, appPath = '.'):
        super().__init__()
        self.defaultAppPath = appPath

    def filesPathScan (self):
        files = []
        # r=root, d=directories, f = files
        for r, d, f in os.walk(self.defaultAppPath):
            for file in f:
                if (r==self.defaultAppPath):
                    files.append(file)
        return files
        
    def fileInfoScan (self, filepath):
        fileInfoResult = {}
        fileMetaStats = os.stat(self.defaultAppPath+'/'+filepath)
        fileInfoResult['name'] = filepath
        fileInfoResult['size'] = fileMetaStats.st_size
        fileInfoResult['lastmodificate'] = fileMetaStats.st_mtime
        return fileInfoResult
    
    def filesInfoScan (self):
        filesInfo2Return=[]
        filespaths = self.filesPathScan()
        for eachFilepath in filespaths:
            if '.py' not in eachFilepath and eachFilepath != "__pycache__":
                filesInfo2Return.append(self.fileInfoScan(eachFilepath))
        return filesInfo2Return

    def testPrintableFilesInfo (self):
        filesInfo = self.filesInfoScan()
        print (filesInfo)

    

    



