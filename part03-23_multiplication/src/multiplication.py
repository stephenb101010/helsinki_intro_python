number = int(input("Please type in a number: "))
y = 1
while y <= number:
    x = 1
    while x <= number:
        print(f"{y} x {x} = {y * x}")
        x += 1
    y += 1