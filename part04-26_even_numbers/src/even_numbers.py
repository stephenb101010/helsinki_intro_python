def even_numbers(my_list: list):
    filtered_list = []
    for num in my_list:
        if num % 2 == 0:
            filtered_list.append(num)    
    return filtered_list