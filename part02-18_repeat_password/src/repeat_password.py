pswd = input("Password: ")
while True:
    repeated_pswd = input("Repeat password: ")
    if pswd == repeated_pswd:
        print("User account created!")
        break
    else:
        print("They do not match!")