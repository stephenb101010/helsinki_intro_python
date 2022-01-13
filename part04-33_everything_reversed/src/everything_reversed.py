def everything_reversed(my_list: list):
    reversed_list = []
    for word in my_list:
        reversed_list.append(word[::-1])
    reversed_list.reverse()
    return reversed_list