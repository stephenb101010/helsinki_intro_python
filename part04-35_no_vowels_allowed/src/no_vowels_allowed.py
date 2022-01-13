def no_vowels(my_string: str):
    vowels = "aeiou"
    return ''.join(letter for letter in my_string if not letter in vowels)

    '''    
    vowels = "aeiou"
    result = ""
    for letter in my_string:
        if letter not in vowels:
            result += letter
    return result'''