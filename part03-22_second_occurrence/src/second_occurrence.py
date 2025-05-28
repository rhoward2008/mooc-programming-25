# Write your solution here
word = input("Please type in a string: ")
sub = input("Please type in a substring: ")

first = word.find(sub)

#print(f'first: {first}')

if first >= 0:
    #print(f'first: {first}')
    #print(f'sec word: {word[first+len(sub):]} ')
    #print(f'second: {word[first+len(sub):].find(sub)}')
    second = word.find(sub,first+len(sub))

else:
    second = -1

if second > 0:
    print(f"The second occurrence of the substring is at index {second}.")
else:
    print("The substring does not occur twice in the string.")
