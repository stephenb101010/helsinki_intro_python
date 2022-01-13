def list_sum(list1: list, list2: list):
    i = 0
    sum_list = []
    while i < len(list1):
        sum_list.append(list1[i] + list2[i])
        i += 1
    return sum_list