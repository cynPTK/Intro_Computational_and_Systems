from sys import argv

income = int(argv[1])
tax = 0

if income < 5000:
    tax = income * 0
elif income > 5000 and income < 15000:
    tax = (income-5000) * .07
elif income > 10000 and income < 30000:
    tax = 700 + (income-15000) * 0.15
elif income >30000:
    tax = 700 + 2250 + (income - 30000)*.25

print(tax)
