from sys import argv

myNum = int(argv[1])

if myNum % 5 == 0 and myNum % 7 ==0:
    print("FizzBizz")
elif myNum % 5 == 0:
    print("Fizz")
elif myNum % 7 == 0:
    print("Bizz")
else:
    print("")
