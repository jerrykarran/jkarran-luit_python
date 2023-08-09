import os     # import the OS module
directoryDictionary = {}

def printDirectoryData(path=os.path.join(os.getcwd())):
    if path[-1] != '/':                                         # check if ending slash is missing
        path = path + '/'
    else:
        currentFileSize = os.path.getsize(path)  
        lastaccess = os.path.getmtime(path)                     # get time file was last accessed
        filedata = [currentFileSize, lastaccess]                # store data in a list
        
        directoryDictionary[path] = filedata                    # add directory folder into dictionary
    origpath = path                                             # hold value of original path
    recursivePrintDirectory(origpath, path)
    for filepath, data in directoryDictionary.items():
        print("{\n\t'path': '" + filepath + "',\n\t'size': '" + str(data[0]) + "',\n\t'last accessed': '" + str(data[1])  + "'\n}\n")

def recursivePrintDirectory(origpath, path):
    directoryList = os.listdir(path) # create a new list of all files and directories
    for currentFileName in directoryList:                       # each file in the directory
        if os.path.isdir(currentFileName):                      # if filename is for a directory 
            if origpath == path:
                fullpathname = path + currentFileName           # get current filename
            else:
                fullpathname = path + '/' + currentFileName     # get current filename with a slash in between
            currentFileSize = os.path.getsize(fullpathname)     # get the size
            lastaccess = os.path.getmtime(fullpathname)         # get time file was last accessed
            filedata = [currentFileSize, lastaccess]            # store data in a list
            
            directoryDictionary[fullpathname] = filedata # creating an entry in the dictionary for this folder
            recursivePrintDirectory(origpath, fullpathname)     # check inside the folder
        elif origpath == path:
            fullpathname = path + currentFileName               # get current filename
            currentFileSize = os.path.getsize(fullpathname)     # get the size
            lastaccess = os.path.getmtime(fullpathname)         # get time file was last accessed
            filedata = [currentFileSize, lastaccess]            # store data in a list
            
            directoryDictionary[fullpathname] = filedata # creating an entry in the dictionary for file
        else:                                                   # not a directory
            fullpathname = path + '/' + currentFileName         # get current filename with a slash in between
            currentFileSize = os.path.getsize(fullpathname)     # get the size
            lastaccess = os.path.getmtime(fullpathname)         # get time file was last accessed
            filedata = [currentFileSize, lastaccess]            # store data in a list
            
            directoryDictionary[fullpathname] = filedata        # creating an entry in the dictionary for other folders and items
        
printDirectoryData('/home/ec2-user/environment/')
