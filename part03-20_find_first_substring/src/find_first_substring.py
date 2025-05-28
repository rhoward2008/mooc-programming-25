# Write your solution here
# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")

first = word.find(char)

if first + 3 <= len(word):
    print(word[first:first+3])