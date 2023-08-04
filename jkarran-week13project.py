import os     # import the OS module

directoryDictionary = {}

def printDirectoryData(path='os.getcwd()'):
    directoryList = os.listdir()
    
    for currentFileName in directoryList: # each file in the directory
        currentFilePath = os.path.abspath(currentFileName)
        currentFileSize = os.path.getsize(currentFileName) # get the size
        directoryDictionary[currentFilePath] = currentFileSize # creating an entry in the dictionary

    for eachEntry in directoryDictionary:
        print("{'path': '" + eachEntry + "', 'size': " + str(directoryDictionary[eachEntry]) + '}')
        
printDirectoryData()