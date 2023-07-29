def testfunction():
    N = 12
    mylist = []
    def insert(inserting, placement, mylist):
        mylist.insert(inserting, placement)
    def myprint(mylist): 
        print(mylist)
    def remove(e, mylist):
        for element in range(len(mylist)):
            if mylist[element] == e:
                del mylist[element]
                return
    def append(e, mylist):
        mylist.append(e)
    def listsort(mylist):
        mylist.sort()   
    def listpop(mylist):
        mylist.pop() 
    def listreverse(mylist):
        mylist.reverse()
        
    for i in range(N):
        userinput = list(input().split(" "))
        if userinput[0] == "insert":
            insert(int(userinput[1]), int(userinput[2]), mylist)
        if userinput[0] == "print":
            myprint(mylist)
        if userinput[0] == "remove":
            remove(int(userinput[1]), mylist)
        if userinput[0] == "append":
            append(int(userinput[1]), mylist)
        if userinput[0] == "sort":
            listsort(mylist)
        if userinput[0] == "pop":
            listpop(mylist)
        if userinput[0] == "reverse":
            listreverse(mylist)
        
testfunction()