def split_and_join(line):
    old = line.split(" ")
    newstring = ''
    
    for i in range (len(old)):
        newstring += old[i]
        if i  != len(old)-1:
            newstring += old[i].join("-")
    return newstring

# if __name__ == '__main__':
#     line = input()
#     result = split_and_join(line)
#     print(result)

a = "this is a string"
print (split_and_join(a))