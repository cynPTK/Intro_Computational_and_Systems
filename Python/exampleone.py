from sys import argv

if argv[1] == "marco":
    print("polo")
elif len(argv[1]) < 5:
    print (argv[1])
else:
    print(argv[1][:5])
