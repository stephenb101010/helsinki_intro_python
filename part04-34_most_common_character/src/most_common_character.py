def most_common_character(my_string: str):
    most_common = ""
    count = 0
    for letter in my_string:
        if my_string.count(letter) > count:
            most_common = letter
            count = my_string.count(letter)
    return most_common

'''    
most_common = my_string[0]
    for character in my_string:
        if my_string.count(character) > my_string.count(most_common):
            most_common = character
    return most_common'''