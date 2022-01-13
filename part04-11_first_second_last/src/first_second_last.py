def first_word(sentence):
    word = ""
    for x in sentence:
        if x != " ":
            word = word + x
        else:
            return word

def second_word(sentence):
    word_start = sentence.find(" ") + 1
    if word_start != -1:
        word_finish = sentence.find(" ", word_start)
        if word_finish == -1:
            word = sentence[word_start:]
        else:
            word = sentence[word_start: word_finish]
    return word

def last_word(sentence):
    last_ind = len(sentence)
    i = last_ind - 1
    while sentence[i] != " ":
        i -= 1
    start_ind = (i + 1)
    word = sentence[start_ind:last_ind]
    return word



# You can test your function by calling it within the following block
if __name__ == "__main__":
    #sentence = "once upon a time there was a programmer"
    sentence = "once upon"
    #print(first_word(sentence))
    print(second_word(sentence))
    #print(last_word(sentence))