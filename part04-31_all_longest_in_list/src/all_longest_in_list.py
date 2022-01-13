def all_the_longest(my_list: list):
    longest_words = []
    my_list.sort(reverse= True, key= len)
    longest = len(my_list[0])
#    longest_words.append(my_list[0])
    for word in my_list:
        if len(word) == longest:
            longest_words.append(word)
    return longest_words