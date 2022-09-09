from sys import *

def RecursiveFactorial(myNum):
    if myNum == 1:
        return 1
    else:
        return myNum * RecursiveFactorial(myNum-1)

bigNum = int(argv[1])
print(RecursiveFactorial(bigNum))
