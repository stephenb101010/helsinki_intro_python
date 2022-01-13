number = int(input("Please type in a positive integer: "))
start_neg = -number
for num in range(start_neg, (number + 1)):
    if num != 0:
        print(num)