def times_ten(start_index: int, end_index: int):
    new_dict = {}
    i = start_index
    while i <= end_index:
        new_dict[i] = i * 10
        i += 1
    return new_dict

'''
    numbers = {}
    for i in range(start_index, end_index + 1): Why don't I remember to use range???????
        numbers[i] = i * 10
    return numbers
'''