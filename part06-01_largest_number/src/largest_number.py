def largest():
    numbers = []
    with open("numbers.txt") as numbers_file:
        for line in numbers_file:
            numbers.append(int(line))
    numbers.sort(reverse= True)
    return numbers[0]

#I definitely like my implementation better. Model below.

'''
    with open("numbers.txt") as file:
        start = True
        biggest = 0
        for number in file:
            if start or int(number) > biggest:
                biggest = int(number)
                start = False
        return biggest
'''