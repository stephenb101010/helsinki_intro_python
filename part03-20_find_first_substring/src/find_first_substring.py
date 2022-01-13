word = input("Please type in a word: ")
letter = input("Please type in a character: ")
exist = letter in word
index = word.find(letter)
length = len(word) - 1
if (exist == True) and (index != -1) and (length >= index + 2):
    print(word[index:index+3])