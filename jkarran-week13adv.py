import os     # import the OS module

directoryDictionary = {}

def printDirectoryData(path=os.path.join(os.getcwd())):
    directoryList = os.listdir(path) # create a new list of all files and directories

    for currentFileName in directoryList:                       # each file in the directory
        currentFilePath = str(os.path.abspath(currentFileName)) # get current path
        fullpath = path + '/' + currentFileName                 # adding the path and current filename
        currentFileSize = os.path.getsize(fullpath)             # get the size
        directoryDictionary[currentFilePath] = currentFileSize  # creating an entry in the dictionary
        
    for p, s in directoryDictionary.items():                    # iterating through the dictionary
        print("{'path': '" + p + "', 'size': " + str(s) + '}')
        
printDirectoryData('/home/ec2-user/environment/.c9')






# directoryDictionary = {}

# def printDirectoryData(path="os.getcwd()"):
#     # if path == "os.getcwd()":
#     #     print("default path, path is: ", path)
#     #     directoryList = os.listdir()
#     # else:
#     #     print("inputted path is:", path, "\n\n")
#     #     directoryList = os.listdir(path)
#     print('path is:', path)
#     print('before')
#     directoryList = os.listdir(path)
#     print('after')
#     for currentFileName in directoryList:                       # each file in the directory
#         currentFilePath = os.path.abspath(currentFileName)      # get the file path 
        
#         if os.path.isdir(currentFileName):                      # check if its a directory
#             print("\n\nits a directory, filename:", currentFileName)
#             printDirectoryData(currentFilePath)                 # if directory, check inside
            
           
#         currentFileSize = os.path.getsize(currentFileName)      # not a directory, lets get the size
#         directoryDictionary[currentFilePath] = currentFileSize  # creating an entry in the dictionary
#         print("added:",currentFilePath,currentFileSize )
    
#     # iterate through the dictionary
#     for p, s in directoryDictionary.items():
#             print("{'path': '" + p + "', 'size': " + str(s) + '}') #full path name and size
            
# printDirectoryData()



# iterate through dictionaries of dictionaries
# for key, value in something.items():
#     print(key, value)
#     for element in value:
#         print(element)
# data_file_path=os.path.join(os.getcwd()




