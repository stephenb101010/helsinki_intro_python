def double_items(numbers: list):
    new_list = []
    for element in numbers:
        new_list.append(element * 2)
    return new_list

'''
def double_items(numbers: list):
    double = numbers[:]
    for i in range(len(double)):
        double[i] *= 2
    return double
'''