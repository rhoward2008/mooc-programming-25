while True:
    text = input("Please type in a string:")
    length = len(text)
    if length == 0:
        break
    else:
        print(text)
        print("-"*length)
