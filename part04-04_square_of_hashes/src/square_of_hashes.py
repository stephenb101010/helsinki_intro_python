# Copy here code of line function from previous exercise
def line(number, text):
    if text == "":
        print("*" * number)
    else:
        print(text[0] * number)

def square_of_hashes(size):
    index = size
    while index > 0:
        # You should call function line here with proper parameters
        line(size, "#")
        index -= 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(5)
