# Write your solution here
password = input("Password")

while True:
    prompt = input("Repeat password")
    if password == prompt:
        print("User account created!")
        break
    else:
        print("They do not match!")
