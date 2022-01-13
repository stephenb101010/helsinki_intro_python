while True:
    number = int(input("Please type in a number: "))
    result = number
    if number <= 0:
        print("Thanks and bye!")
        break
    else:
        factorial = number
        while factorial > 1:
            result *= (factorial - 1)
            factorial -= 1
        print(f"The factorial of the number {number} is {result}")