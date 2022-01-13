usr_string = input("Please type in a string: ")
length = len(usr_string)
index = 0
while index < length:
    print(usr_string[:index + 1])
    index += 1