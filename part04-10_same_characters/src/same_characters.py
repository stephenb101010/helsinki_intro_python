def same_chars(text, num0, num1):
    if ((len(text) - 1) < num0) or ((len(text) - 1) < num1):
        return False
    else:
        ind0 = text[num0]
        ind1 = text[num1]
        if (ind0 == ind1):
            return True
        else:
            return False

# You can test your function by calling it within the following block
if __name__ == "__main__":
    print(same_chars("abc", 0, 3))