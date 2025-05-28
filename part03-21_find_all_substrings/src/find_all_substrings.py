# Write your solution here
# Write your solution here
word = input("Please type in a word: ")
char = input("Please type in a character: ")

position = []

for p,c in enumerate(word):
    if c == char:
        position.append(p)

#print(f'position: {position}')

for i in position:
    #print(f'loop: i: {i}')
    if len(word)-i >=3:
        print(word[i:i+3])
