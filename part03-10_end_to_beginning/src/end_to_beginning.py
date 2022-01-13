usr_string = input("Please type in a string: ")
countdown = len(usr_string)
index = 0
while index < countdown:
    print(usr_string[countdown - 1])
    countdown -= 1