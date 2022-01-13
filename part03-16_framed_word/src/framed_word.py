usr_word = input("Word: ")
start = (28 - len(usr_word)) // 2

if len(usr_word) % 2 == 0:
    end = start
else:
    end = start+1

print('*' * 30)
print(f"*{(start * ' ')}{usr_word}{(end * ' ')}*")
print('*' * 30)