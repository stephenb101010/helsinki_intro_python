# Write your solution here
number = int(input("Please type in a number: "))
end = "Thank you!"
if number < 1000:
    print("This number is smaller than 1000")
    if number < 100:
        print("This number is smaller than 100")
        if number < 10:
            print("This number is smaller than 10")
    print(end)
else:
    print(end)