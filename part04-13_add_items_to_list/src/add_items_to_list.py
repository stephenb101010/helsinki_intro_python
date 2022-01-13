list_size = int(input("How many items: "))
i = 1
list = []
while list_size > 0:
    add_value = int(input(f"Item {i}: "))
    list.append(add_value)
    i += 1
    list_size -= 1
print(list)