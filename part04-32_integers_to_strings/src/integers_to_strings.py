def formatted(my_list: list):
    new_list = []
    for num in my_list:
        #remember to combine expressions where possible
        num = f"{num:.2f}"
        new_list.append(num)
    return new_list

'''    
    result = []
    for number in my_list:
        result.append(f"{number:.2f}")
    return result'''