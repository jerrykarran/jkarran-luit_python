import os     # import the OS module

directoryDictionary = {}

def printDirectoryData(path='os.getcwd()'):
    directoryList = os.listdir()
    
    for currentFileName in directoryList: # each file in the directory
        currentFilePath = os.path.abspath(currentFileName)
        currentFileSize = os.path.getsize(currentFileName) # get the size
        directoryDictionary[currentFilePath] = currentFileSize # creating an entry in the dictionary

    for p, s in directoryDictionary.items():
        print("{'path': '" + p + "', 'size': " + str(s) + '}')
        
printDirectoryData()



# def printDirectoryData2(path='os.getcwd()'):
#     # if path == 'os.getcwd()':
#     #     directoryList = os.listdir()
#     # else:
#     #     directoryList = os.listdir(path)
    
    
#     directoryList = os.listdir(path) 
#     for currentFileName in directoryList: # each file in the directory  
#         currentFilePath = os.path.abspath(currentFileName)
#         currentFileSize = os.path.getsize(currentFileName) # get the size
#         # currentFileSize2 = os.path.getsize(currentFilePath) # get the size
#         directoryData[currentFileName] = currentFileSize # creating an entry
        
#         # print('filename:', currentFileName + '\nfilenamesize: ' + str(currentFileSize) +  '\n\ncurrentFilePath:', currentFilePath, '\nfilepathsize: ' + str(currentFileSize2) + '\n')
        
        
#         # print("{'path': '" + currentFilePath + "', 'size': " + str(currentFileSize))
        
#         # print("{'path': '" + currentFilePath + "', 'namesize': " + str(currentFileSize) + ", 'pathsize': " + str(currentFileSize2) + '}')
    
# printDirectoryData2('/home/ec2-user/')





def printDirectoryData3(path='os.getcwd()'):

    if path == 'os.getcwd()':
        directoryList = os.listdir()
    else:
        directoryList = os.listdir(path)
    
    for currentFileName in directoryList: # each file in the directory
        currentFilePath = os.path.abspath(currentFileName)
        currentFileSize = os.path.getsize(currentFileName) # get the size
        directoryData[currentFilePath] = currentFileSize # creating an entry in the dictionary
        # print("{'path': '" + currentFilePath + "', 'size': " + str(currentFileSize) + '}')

    for p, s in directoryDictionary.items():
        print("{'path': '" + p + "', 'size': " + str(s) + '}')
        

# printDirectoryData3("/home/ec2-user/")