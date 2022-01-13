def anagrams(word_0, word_1):
    if len(word_0) == len(word_1):
        if sorted(word_0) == sorted(word_1):
            return True
        else:
            return False
    else:
        return False

if __name__ == "__main__":
    print(anagrams("tame", "meta"))
    print(anagrams("tame", "mate"))
    print(anagrams("tame", "team"))
    print(anagrams("tabby", "batty"))
    print(anagrams("python", "java"))