def isPal(inputString):
    i=0
    if (inputString == inputString[::-1]):
        return True
    return False

print(isPal("racecar"))
