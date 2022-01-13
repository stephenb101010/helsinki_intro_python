print("Please type in integer numbers. Type in 0 to finish.")
count = 0
sum_total = 0
positives = 0
negatives = 0
while True:
    number = int(input("Number: "))
    if number == 0:
        print(f"Numbers typed in {count}")
        print(f"The sum of the numbers is {sum_total}")
        print(f"The mean of the numbers is {sum_total / count}")
        print(f"Positive numbers {positives}")
        print(f"Negative numbers {negatives}")
        break
    else:
        count += 1
        sum_total += number
        if number > 0:
            positives +=1
        else:
            negatives +=1
