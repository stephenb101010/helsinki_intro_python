# Copy here code of line function from previous exercise and use it in your solution
def line(number, text):
    if text == "":
        print("*" * number)
    else:
        print(text[0] * number)

def triangle(size, text):
    index = 1
    while index <= size:
        line(index, text)
        index += 1

def rectangle(width, height, character):
    index = height
    while index > 0:
    # You should call function line here with proper parameters
        line(width, character)
        index -= 1

def shape(width, text, height, filler):
    if height == 0:
        triangle(width, text)
    else:
        triangle(width, text)
        rectangle(width, height, filler)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    shape(5, "x", 2, "o")