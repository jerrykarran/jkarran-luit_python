import os     # import the OS module

directoryDictionary = {}

def printDirectoryData(path=os.path.join(os.getcwd())):
    # print('path:', path)
    recursivePrintDirectory(path)
    
    for p, s in directoryDictionary.items():                    # iterating through the dictionary
        print("{'path': '" + p + "', 'size': " + str(s) + '}')



def recursivePrintDirectory(path=os.path.join(os.getcwd())):
    directoryList = os.listdir(path) # create a new list of all files and directories

    for p, s in directoryDictionary.items():                    # iterating through the dictionary
        if os.path.isdir(currentFileName):                      # if filename is for a directory 
            fullpath = path +  currentFileName                  # adding the path and current filename
            # print('in if, folder')
            recursivePrintDirectory(fullpath)
        elif len(directoryList) == 0:
            print("333333")
            currentFileSize = os.path.getsize(path)
            directoryDictionary[pathname] = currentFileSize  # creating an entry in the dictionary

        else:
            print("length:", len(dire))
            pathname = path + '/' + currentFileName
            currentFileSize = os.path.getsize(pathname)             # get the size
            # print('pathname', pathname)
            
            directoryDictionary[pathname] = currentFileSize  # creating an entry in the dictionary
        
    
        
printDirectoryData('/home/ec2-user/environment/')