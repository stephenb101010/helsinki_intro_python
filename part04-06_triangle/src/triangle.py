# Copy here code of line function from previous exercise
def line(number, text):
    if text == "":
        print("*" * number)
    else:
        print(text[0] * number)

def triangle(size):
    index = 1
    while index <= size:
        line(index, "#")
        index += 1

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(5)
