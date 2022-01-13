def distinct_numbers(my_list: list):
    my_set = set(my_list)
    my_new_list = list(my_set)
    my_new_list.sort()
    return my_new_list

""" 
model solution using iteration

    results = []
    for item in my_list:
        if item not in results:
            results.append(item)
    results.sort()
    return results """