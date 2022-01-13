# Write your solution here
first_number = int(input("Please type in the first number: "))
another_number = int(input("Please type in another number: "))
if first_number == another_number:
    print("The numbers are equal!")
elif first_number > another_number:
    print(f"The greater number was {first_number}")
else:
    print(f"The greater number was {another_number}")