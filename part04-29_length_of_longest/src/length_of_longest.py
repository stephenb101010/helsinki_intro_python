def length_of_longest(my_list: list):
    length = 0
    for word in my_list:
        if len(word) > length:
            length = len(word)
    return length