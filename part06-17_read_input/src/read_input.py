def read_input(message, low, high):
    while True:
        try:
            num = int(input(message))
            if num >= low and num <= high:
                return num
        except ValueError:
            pass

        print(f'You must type in an integer between {low} and {high}')

'''
def read_input(prompt: str, lower_limit: int, upper_limit: int):

    while True:

        error = False

        try:

            number = int(input(prompt))

            if number < lower_limit or number > upper_limit:

                error = True

        except:

            error = True

        if error:

            print(f"You must type in an integer between {lower_limit} and {upper_limit}")

        else:

            return number
'''