def remove_smallest(numbers: list):
    copy = []
    for element in numbers:
        copy.append(element)
    copy.sort()
    numbers.remove(copy[0])

'''
def remove_smallest(numbers: list):
    #I forgot about min() for lists - grrrrr
    smallest = min(numbers)
    numbers.remove(smallest)
'''