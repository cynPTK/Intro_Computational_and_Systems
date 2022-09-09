from sys import argv
password = argv[1]
if (len(password) < 12 or len(password) > 16):
    print ("Invalid")
else:
    upcounter = 0
    lowcounter = 0
    number = 0
    for i in password:
        if i.isupper():
            upcounter+=1
        elif i.islower():
            lowcounter+=1
        elif i.isnumeric():
            number+=1
    if upcounter < 2 or lowcounter < 4 or number < 1:
        print("Invalid")
    else:
        print("Valid")
