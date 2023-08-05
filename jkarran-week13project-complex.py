import os     # import the OS module

directoryDictionary = {}

def printDirectoryData(path=os.path.join(os.getcwd())):
    addslash = True
    if (path == os.path.join(os.getcwd())):
        addslash = False
        
        # print('path:', path)
    origpath = path                         # check if this the main path
    
    recursivePrintDirectory(origpath, addslash, path)
    
    for p, s in directoryDictionary.items():                    # iterating through the dictionary
        print("{'path': '" + p + "', 'size': " + str(s) + '}')

def recursivePrintDirectory(origpath, addslash, path=os.path.join(os.getcwd())):
    directoryList = os.listdir(path) # create a new list of all files and directories
    
    for currentFileName in directoryList:                       # each file in the directory
        if os.path.isdir(currentFileName):                      # if filename is for a directory 
            if addslash:
                fullpath = path + '/' + currentFileName             # adding the path and current filename
                currentFileSize = os.path.getsize(fullpath)             # get the size
                fullpath = path + currentFileName 
                print('in if 1 gets double')
            else:
                fullpath = path + '/' + currentFileName 
                currentFileSize = os.path.getsize(fullpath)             # get the size
            directoryDictionary[fullpath] = currentFileSize     # creating an entry in the dictionary for this folder
            recursivePrintDirectory(origpath, addslash, fullpath)         # check inside the folder
        
        elif origpath == path:
            # currentFilePath = os.path.abspath(currentFileName)
            # currentFileSize = os.path.getsize(currentFileName)      # get the size
            # directoryDictionary[currentFilePath] = currentFileSize  # creating an entry in the dictionary
            if addslash:
                print('in if 2')
                pathname = path + '/' + currentFileName
                currentFileSize = os.path.getsize(pathname)         # get the size
                if path != os.getcwd():
                    pathname = path + currentFileName
                    print('not equal inside')
            else:
                pathname = path + '/' + currentFileName
                currentFileSize = os.path.getsize(pathname)         # get the size
            directoryDictionary[pathname] = currentFileSize     # creating an entry in the dictionary for items in main directory
        
        else:
            pathname = path + '/' + currentFileName
            currentFileSize = os.path.getsize(pathname)         # get the size
            # print('pathname', pathname)
            directoryDictionary[pathname] = currentFileSize     # creating an entry in the dictionary for other folders and items
        
    
        
printDirectoryData('/home/ec2-user/environment/.c9')
# print('\n\n')
# printDirectoryData()