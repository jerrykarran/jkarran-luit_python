import os     # import the OS module
directoryDictionary = {}

def printDirectoryData(path=os.path.join(os.getcwd())):
    if path[-1] != '/':                                         # check if ending slash is missing
        path = path + '/'
    else:
        currentFileSize = os.path.getsize(path)     
        directoryDictionary[path] = currentFileSize             # add directory folder into dictionary
    origpath = path                                             # hold value of original path
    recursivePrintDirectory(origpath, path)
    for p, s in directoryDictionary.items():                    # iterating through the dictionary
        print("{'path': '" + p + "', 'size': " + str(s) + '}')

def recursivePrintDirectory(origpath, path):
    directoryList = os.listdir(path) # create a new list of all files and directories
    for currentFileName in directoryList:                       # each file in the directory
        if os.path.isdir(currentFileName):                      # if filename is for a directory 
            if origpath == path:
                fullpathname = path + currentFileName           # get current filename
            else:
                fullpathname = path + '/' + currentFileName     # get current filename with a slash in between
            currentFileSize = os.path.getsize(fullpathname)     # get the size

            directoryDictionary[fullpathname] = currentFileSize # creating an entry in the dictionary for this folder
            recursivePrintDirectory(origpath, fullpathname)     # check inside the folder
        elif origpath == path:
            fullpathname = path + currentFileName               # get current filename
            currentFileSize = os.path.getsize(fullpathname)     # get the size
            directoryDictionary[fullpathname] = currentFileSize # creating an entry in the dictionary for file
        else:                                                   # not a directory
            fullpathname = path + '/' + currentFileName         # get current filename with a slash in between
            currentFileSize = os.path.getsize(fullpathname)     # get the size
            directoryDictionary[fullpathname] = currentFileSize # creating an entry in the dictionary for other folders and items
        
printDirectoryData('/home/ec2-user/environment/')