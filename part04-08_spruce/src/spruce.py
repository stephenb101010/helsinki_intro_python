def spruce(height):
    print("a spruce!")
    index = 1
    space = height - 1
    width = ((2 * height) - 1)
    while index <= width:
        print((" " * space) + ("*" * index))
        index += 2
        space -= 1
    print((" " * (height - 1)) + ("*" * 1))
# You can test your function by calling it within the following block
if __name__ == "__main__":
    spruce(5)