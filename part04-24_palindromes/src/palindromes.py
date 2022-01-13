def palindromes(word: str):
    letters = "".join(x for x in word if x.isalpha()).lower()
    reversed_letters = letters[::-1]
    return letters == reversed_letters


def palindrome_candidate():
    while word := input("Please enter a word: "):
        yield word

def main():
    for word in palindrome_candidate():
        if palindromes(word):
            print(f"{word} is a palindrome!")
            break
        else:
            print("that wasn't a palindrome")

#if __name__ == "__main__":
main()