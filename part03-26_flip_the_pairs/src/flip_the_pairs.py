number = int(input("Please type in a number: "))
x = 0
while x <= number:
    if (x + 2) <= number:
        print(x + 2)
    x += 2
    if (x - 1) <= number:
        print(x - 1)