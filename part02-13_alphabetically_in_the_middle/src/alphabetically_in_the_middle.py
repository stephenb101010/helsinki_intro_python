# Write your solution here
first = input("1st letter: ")
second = input("2nd letter: ")
third = input("3rd letter: ")
middle = ""
if (first > second > third) or (third > second > first):
    middle = second
elif (first > third > second) or (second > third > first):
    middle = third
else:
    middle = first
print(f"The letter in the middle is {middle}")