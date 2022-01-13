from math import sqrt
while True:
    input_number = int(input("Please type in a number: "))
    if input_number == 0:
        print("Exiting...")
        break
    elif input_number < 0:
        print("Invalid number")
    else:
        print(sqrt(input_number))