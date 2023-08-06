import os     # import the OS module

directoryDictionary = {}

def printDirectoryData(path=os.path.join(os.getcwd())):
    directoryList = os.listdir(path)                            # create a new list of all files and directories

    for currentFileName in directoryList:                       # each file in the directory
        fullpath = path + '/' + currentFileName                 # adding the slash between the path and current filename
        currentFileSize = os.path.getsize(fullpath)             # get the size
        lastaccess = os.path.getmtime(currentFileName)          # get time file was last accessed
        filedata = [currentFileSize, lastaccess]                # store data in a list
        directoryDictionary[fullpath] = filedata         # creating an entry in the dictionary
        
    for filepath, data in directoryDictionary.items():                    # iterating through the dictionary
        print("{'path': '" + filepath + "', 'size': '" + str(data[0]) + "', 'last accessed': '" + str(data[1])  + "'}")
        
# printDirectoryData('/home/ec2-user/environment/.c9')
printDirectoryData()