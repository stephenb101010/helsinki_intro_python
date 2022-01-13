# Write your solution here
value = int(input("Value of gift: "))
tax_paid = 0
if (value < 5000):
    print("No tax!")
elif (5000 <= value < 25000):
    tax_paid = (100 + ((value - 5000) * 0.08))
    print(f"Amount of tax: {tax_paid} euros")
elif (25000 <= value < 55000):
    tax_paid = (1700 + ((value - 25000) * 0.10))
    print(f"Amount of tax: {tax_paid} euros")
elif (55000 <= value < 200000):
    tax_paid = (4700 + ((value - 55000) * 0.12))
    print(f"Amount of tax: {tax_paid} euros")
elif (200000 <= value < 1000000):
    tax_paid = (22100 + ((value - 200000) * 0.15))
    print(f"Amount of tax: {tax_paid} euros")
elif (1000000 <= value):
    tax_paid = (142100 + ((value - 1000000) * 0.17))
    print(f"Amount of tax: {tax_paid} euros")