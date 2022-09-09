from sys import argv

query = argv[1]
Filename = argv[2]

for line in open(FileName, "r"):
    if query in line:
        print (line)
