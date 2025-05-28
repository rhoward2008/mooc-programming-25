# Write your solution here
while True:
    editor = input("Editor:").lower()
    
    if editor == "visual studio code":
        print("an excellent choice!")
        break
    elif editor in ["word","notepad"]:
        print("awful")
    else:
        print("not good")