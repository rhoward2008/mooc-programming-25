# Write your solution here
word = input("Please input a string:")

if len(word) >= 2:
    if word[1] == word[-2]:
        print(f'The second and the second to last characters are {word[1]}')
    else:
        print("The second and the second to last characters are different")
else:
    print("Word too short")