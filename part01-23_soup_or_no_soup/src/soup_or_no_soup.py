# Write your solution here
name = input("Please tell me your name: ")
next = "Next please!"
if name == "Jerry":
    print(next)
else:
    portion_number = int(input("How many portions of soup?"))
    portion_price = 5.9
    print(f"The total cost is {portion_number * portion_price}")
    print(next)