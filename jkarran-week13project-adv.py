import os     # import the OS module

directoryDictionary = {}

def printDirectoryData(path=os.path.join(os.getcwd())):
    directoryList = os.listdir(path)                            # create a new list of all files and directories

    for currentFileName in directoryList:                       # each file in the directory
        fullpath = path + '/' + currentFileName                 # adding the slash between the path and current filename
        currentFileSize = os.path.getsize(fullpath)             # get the size
        directoryDictionary[fullpath] = currentFileSize         # creating an entry in the dictionary
        
    for p, s in directoryDictionary.items():                    # iterating through the dictionary
        print("{'path': '" + p + "', 'size': " + str(s) + '}')
        
# printDirectoryData('/home/ec2-user/environment/.c9')
printDirectoryData()