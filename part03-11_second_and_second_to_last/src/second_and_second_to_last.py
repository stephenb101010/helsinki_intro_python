usr_string = input("Please type in a string: ")
response = "The second and the second to last characters are "
second = usr_string[1]
second_to_last = usr_string[-2]
if second == second_to_last:
    print(response + second)
else:
    print(response + "different")