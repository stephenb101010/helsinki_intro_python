def compare_dot(word_with_dot, word):
    same = True
    for i in range(len(word)):
        if word_with_dot[i] != '.' and word_with_dot[i] != word[i]:
            same = False
    return same

def find_words(search_term: str):
    found_terms = []

    with open('words.txt') as file:
        for line in file:
            line = line.replace('\n', '')
            word = line.strip()
            if ('.' in search_term) and len(search_term) == len(word):
                if compare_dot(search_term, word) == True:
                    found_terms.append(word)
            elif search_term.startswith('*'):
                if word.endswith(search_term[1:]):
                    found_terms.append(word)
            elif search_term.endswith('*'):
                if word.startswith(search_term[:-1]):
                    found_terms.append(word)
            else:
                if search_term == word:
                    found_terms.append(word)

    return found_terms
if __name__ == "__main__":
    print(find_words('acq*'))

'''
def find_words(search_term: str):

    results = []

 

    with open("words.txt") as file:

        # Tätä tarvitaan myöhemmin

        hakusana_ilman_tahtea = search_term.replace("*","")

 

        for word in file:

            word = word.replace("\n","")

            # Is there an asterisk?

            if "*" in search_term:

                # start or end?

                if search_term[0] == "*":

                    if word.endswith(hakusana_ilman_tahtea):

                        results.append(word)

                else:

                    if word.startswith(hakusana_ilman_tahtea):

                        results.append(word)

            # Is there a dot?

            elif "." in search_term:

                # same length?

                if len(search_term) == len(word):

                    found = True

                    for i in range(len(search_term)):

                        if search_term[i] != "." and search_term[i] != word[i]:

                            found = False

                            break

                    if found:

                        results.append(word)

            # No special characters, only whole word matches count

            else:

                if word == search_term:

                    results.append(word)

    return results
'''