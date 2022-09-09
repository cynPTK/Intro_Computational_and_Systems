from sys import *

def IsPrime(i):
    for possibleFactor in range(2,i):
        if i % possibleFactor == 0:
            return False
        return True

BigNum = int(argv[1])
for i in range(2, BigNum):
    if IsPrime(i):
        print(i)
