
def printList(myList):
    outlist = []
    for el in myList:
        outlist.append(str(el))
    print("\t".join(outlist))

firstline = ["1", "|"] + list(range(2,11))
printList(firstline)
print("-"*80)
for i in range (2,11):
    cutLine = [str(i), "|"]
    for j in range(2,11):
        cutLine.append(i*j)
    printList(cutLine)

