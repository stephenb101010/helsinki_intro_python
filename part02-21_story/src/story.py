previous = ""
words = ""
while True:
    word = input("Please type in a word: ")
    if word != "end" and word != previous:
        words += word + " "
        previous = word
    else:
        print(words)
        break