string_0 = input("Please type in string 1: ")
string_1 = input("Please type in string 2: ")
if len(string_0) == len(string_1):
    print("The strings are equally long")
elif len(string_0) > len(string_1):
    print(f"{string_0} is longer")
else:
    print(f"{string_1} is longer")