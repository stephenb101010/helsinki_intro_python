def line(number, text):
    if text == "":
        print("*" * number)
    else:
        print(text[0] * number)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    line(5, "x")