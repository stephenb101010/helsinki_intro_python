limit = int(input("Limit: "))
output = 1
initial = 2
consecutive_sum = "1 "
while output < limit:
    consecutive_sum += f" + {initial}"
    output += initial
    initial += 1
print(f"The consecutive sum: {consecutive_sum} = {output}")