sentence = input("Please type in a sentence: ")
limit = len(sentence)
index = 0
print(sentence[0])
while (index < limit):
    if sentence[index] == " ":
        print(sentence[index + 1])
    index += 1