import os

class FileManager:

    def __init__(self):
        super().__init__()

    def fileInfoScan (self, filepath):
        fileInfoResult = {}
        fileMetaStats = os.stat(filepath)
        fileInfoResult['name'] = os.path.basename(filepath)
        fileInfoResult['size'] = fileMetaStats.st_size
        fileInfoResult['lastmodificate'] = fileMetaStats.st_mtime
        return fileInfoResult