list = []
while True:
    item = int(input("New item: "))
    if item == 0:
        print("Bye!")
        break      
    else:
        list.append(item)
        print(f"The list now: {list}")
        print(f"The list in order: {sorted(list)}")