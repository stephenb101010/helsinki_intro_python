from string import ascii_lowercase
from random import randint, shuffle

def generate_strong_password(length: int, contain_numbers: bool, contain_specialchars: bool):
    how_many_lowercase_chars = 1
    how_many_numbers = 0
    how_many_specialchars = 0

    if contain_numbers == True and contain_specialchars == True:
        how_many_numbers = randint(1, length-2)
        max_specialchars = length - 1 - how_many_numbers
        how_many_specialchars = randint(1, max_specialchars)
        how_many_lowercase_chars = length - how_many_numbers - how_many_specialchars
    elif contain_numbers == True:
        how_many_numbers = randint(1, length-1)
        how_many_lowercase_chars += (length - 1 - how_many_numbers)
    elif contain_specialchars == True:
        how_many_specialchars = randint(1, length-1)
        how_many_lowercase_chars += (length - 1 - how_many_specialchars)
    else:
        how_many_lowercase_chars = length

    password = []
    special_chars = list('!?=+-()#')
    lowercase_chars = list(ascii_lowercase)

    for i in range(how_many_numbers):
        password.append(str(randint(0, 9)))

    for i in range(how_many_specialchars):
        random_index = randint(0, len(special_chars)-1)
        password.append(special_chars[random_index])

    for i in range(how_many_lowercase_chars):
        random_index = randint(0, len(lowercase_chars)-1)
        password.append(lowercase_chars[random_index])

    shuffle(password)

    return ''.join(password) 