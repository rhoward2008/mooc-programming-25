# Write your solution here

text = input("Please type in a string:")
length = len(text)

if length % 2 == 0:
    white_start = white_end = int((28 - length) / 2)
else:
    white_start = int((28 - length) // 2)
    white_end = int(white_start + 1)

print("*"*30)
print(f'*{" " * white_start}{text}{" " * white_end}*')
print("*"*30)
