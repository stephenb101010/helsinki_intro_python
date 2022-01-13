#I don't like starting off with an inifnite loop but that's what the assignment calls for.
while True:
    editor = input("Editor: ")
    if editor.lower() == "visual studio code":
        print("an excellent choice!")
        break
    elif editor.lower() == (("word") or ("notepad")):
        print("awful")
    else:
        print("not good")