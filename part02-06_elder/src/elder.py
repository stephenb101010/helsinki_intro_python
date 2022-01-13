# Write your solution here
print("Person 1:")
first_person = input("Name: ")
first_age = int(input("Age: "))
print("Person 2:")
second_person = input("Name: ")
second_age = int(input("Age: "))
if first_age == second_age:
    print(f"{first_person} and {second_person} are the same age")
elif first_age > second_age:
    print(f"The elder is {first_person}")
else:
    print(f"The elder is {second_person}")