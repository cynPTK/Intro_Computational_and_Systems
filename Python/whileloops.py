from sys import argv
i = 0
while i <= len(argv[1]):
    argv[1] = argv[1][:-1]
    print(argv[1])
    i++
