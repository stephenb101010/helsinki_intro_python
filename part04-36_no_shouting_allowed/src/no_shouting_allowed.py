def no_shouting(my_list: list):
    new_list = []
    for word in my_list:
        if word.isupper() == False:
            new_list.append(word)
        #don't need else for just continuing
#        else:
#            continue
    return new_list