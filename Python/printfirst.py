def deduplicate(myList):
    outList = []
    myDict = {}
    for item in myList:
        if item not in myDict:
            myDict[item] = 0
            outList.append(item)
    return outList

print(deduplicate(([1,1,4,5,5,34]))
