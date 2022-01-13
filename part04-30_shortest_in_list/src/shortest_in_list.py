def shortest(my_list: list):
    smallest = my_list[0]
    for word in my_list:
        if len(word) < len(smallest):
            smallest = word
    return smallest