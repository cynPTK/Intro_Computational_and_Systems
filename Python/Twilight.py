from sys import argv

MyDict = {}

for line in open(argv[1], "r"):
    words = line.strip().split()
    for word in words:
        if word not in MyDict:
            MyDict[word] = 0
        MyDict[word] += 1

outList = []
for key in MyDict:
    outList.append([MyDict[key], key])
    #print(key + "\t" + str(MyDict[key]))

outList.sort
print(outList)
