list = []
i = 1
print(f"The list is now {list}")
while True:
    
    option = input("a(d)d, (r)emove or e(x)it: ")
    if option == "x":
        print("Bye!")
        break
    elif option == "d":
        list.append(i)
        i += 1
        print(f"The list is now {list}")
    else:
        i -= 1
        list.remove(i)
        print(f"The list is now {list}")