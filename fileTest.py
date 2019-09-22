from app_infrastructure.resourceManagement.resourceDirectoryManagement import resourceDirectoryManager
from app_infrastructure.cacheManagement.cacheDirectoryManagement import cacheDirectoryManager
from app_infrastructure.cacheManagement.cacheFilesManagement import cacheFilesManager
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

resDirectory = 'filesDir.json'
resRoot = './files/'
cacheDirectory = 'cacheDir.json'
cacheRoot = './cache/'
localHost = '192.168.0.1'

resDirManager = resourceDirectoryManager(resDirectory, resRoot,False)
directory = resDirManager.scanDirectory()
cachDirManeger = cacheDirectoryManager(cacheDirectory)
cachFilesManager = cacheFilesManager(cacheRoot, resRoot)

guiActive = True

while guiActive:
    coounter = 0
    for file in directory:
        print(str(coounter)+': '+file['name'] + '\n')
        coounter = coounter+1
    print ('select a file index from list and press enter:')
    fileIndex = int(input())
    cacheFileInfo = cachDirManeger.createCacheDirectory(directory[fileIndex], localHost)
    cachFilesManager.createCacheFiles(cacheFileInfo)
