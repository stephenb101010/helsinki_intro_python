def longest(strings: list):
    strings.sort(reverse= True, key= len)
    longest = strings[0]
    return longest