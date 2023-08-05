import os     # import the OS module

directoryDictionary = {}

def printDirectoryData(path=os.path.join(os.getcwd())):
    directoryList = os.listdir(path) # create a new list of all files and directories

    for currentFileName in directoryList:                       # each file in the directory
        fullpath = path + '/' + currentFileName                 # adding the path and current filename to get the full path
        # print('in for:', 'fullpath', fullpath )
        if os.path.isdir(currentFileName):                      # check if its a directory
            # print("\n\nits a directory, fullpath:", fullpath)
            printDirectoryData(fullpath)                        # if directory, check inside
        else:
            currentFileSize = os.path.getsize(fullpath)         # not a directory, get the size
            directoryDictionary[fullpath] = currentFileSize     # add an entry in the dictionary
        
    for p, s in directoryDictionary.items():                    # iterating through the dictionary
        print("{'path': '" + p + "', 'size': " + str(s) + '}')

        
printDirectoryData()




# iterate through dictionaries of dictionaries
# for key, value in something.items():
#     print(key, value)
#     for element in value:
#         print(element)

# data_file_path=os.path.join(os.getcwd()