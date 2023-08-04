import os     # import the OS module

directoryDictionary = {}

def printDirectoryData(path='os.getcwd()'):
    directoryList = os.listdir()
    
    for currentFileName in directoryList: # each file in the directory
        currentFilePath = os.path.abspath(currentFileName)
        currentFileSize = os.path.getsize(currentFilePath) # get the size
        directoryDictionary[currentFilePath] = currentFileSize # creating an entry in the dictionary

    for p, s in directoryDictionary.items():
        print("{'path': '" + p + "', 'size': " + str(s) + '}')
        
printDirectoryData()