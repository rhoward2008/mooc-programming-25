# Write your solution here
mystring = input("Please type in a string:")

vowels = ['a','e','o']

for i in vowels:
    if i in mystring:
        print(f'{i} found')
    else:
        print(f'{i} not found')