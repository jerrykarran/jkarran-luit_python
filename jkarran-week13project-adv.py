import os     # import the OS module
# import pprint # import this for print formatting
directoryData = {}

def printDirectoryData(path='os.getcwd()'):
    directoryList = os.listdir()
    
    for currentFileName in directoryList: # each file in the directory
        currentFilePath = os.path.abspath(currentFileName)
        currentFileSize = os.path.getsize(currentFileName) # get the size
        directoryData[currentFilePath] = currentFileSize # creating an entry in the dictionary
        # print("{'path': '" + currentFilePath + "', 'size': " + str(currentFileSize) + '}')

    for each in directoryData:
        print("{'path': '" + each + "', 'size': " + str(directoryData[each]) + '}')
        

# printDirectoryData()




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

    for each in directoryData:
        print("{'path': '" + each + "', 'size': " + str(directoryData[each]) + '}')
        

printDirectoryData3("/home/ec2-user/")