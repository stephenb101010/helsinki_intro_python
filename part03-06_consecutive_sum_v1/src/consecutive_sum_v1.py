limit = int(input("Limit: "))
output = 1
initial = 2
while output < limit:
    output += initial
    initial += 1
print(output)