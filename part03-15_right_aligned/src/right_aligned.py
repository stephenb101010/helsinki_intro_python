usr_string = input("Please type in a string: ")
length = len(usr_string)
diff = (20 - length)
if diff > 0:
    starry_line = "*" * diff
    print(starry_line + usr_string)
else:
    print(usr_string)