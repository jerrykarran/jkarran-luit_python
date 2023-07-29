import os     # import the OS module
import pprint # import this for print formatting
directoryData = {}

def printDirectoryData():
    directoryList = os.listdir()
    for currentFileName in directoryList:
        currentFilesize = os.path.getsize(currentFileName)
        directoryData[currentFileName] = currentFilesize
    pprint.pprint(directoryData)
    
printDirectoryData()



# def printDirectoryData(path='os.getcwd()'):
#     if path == 'os.getcwd()':
#         directoryList = os.listdir()
#     else:
#         directoryList = os.listdir(path)
#     for currentFileName in directoryList:
#         currentFilesize = os.path.getsize(currentFileName)
#         directoryData[currentFileName] = currentFilesize
#     pprint.pprint(directoryData)
    
# printDirectoryData('/Users/jerry/Desktop')