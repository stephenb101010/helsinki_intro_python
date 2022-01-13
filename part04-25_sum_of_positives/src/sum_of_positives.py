def sum_of_positives(my_list: list):
    filtered_list = []
    for num in my_list:
        if num >  0:
            filtered_list.append(num)
    return sum(filtered_list)