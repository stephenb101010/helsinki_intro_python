number = int(input("Please type in a number: "))
index = 0
while (index < number):
    index += 1
    print(index)
    if index == number:
        break
    print(number)
    number -= 1