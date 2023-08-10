import os     # import the OS module

directoryDictionary = {}

def printDirectoryData(path='os.getcwd()'):
    directoryList = os.listdir()
    
    for currentFileName in directoryList:                       # each file in the directory
        currentFilePath = os.path.abspath(currentFileName)
        currentFileSize = os.path.getsize(currentFileName)      # get the size
        lastaccess = os.path.getmtime(currentFileName)          # get time file was last accessed
        filedata = [currentFileSize, lastaccess]                # store data in a list
        directoryDictionary[currentFilePath] = filedata         # creating an entry in the dictionary

    for filepath, data in directoryDictionary.items():
        print("{\n\t'path': '" + filepath + "',\n\t'size': '" + str(data[0]) + "',\n\t'last accessed': '" + str(data[1])  + "'\n}\n")
        
printDirectoryData()