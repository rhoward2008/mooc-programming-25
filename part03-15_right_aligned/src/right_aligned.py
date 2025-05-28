# Write your solution here

text = input("Please type in a string:")
length = len(text)

if length < 20:
    print(f'{"*"*(20-length)}{text}')
else:
    print(text)