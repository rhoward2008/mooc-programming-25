# Write your solution here
word1 = input("Please type in string 1:")
word2 = input("Please type in string 2:")

len1 = len(word1)
len2 = len(word2)

if len1 == len2:
    print("The strings are equally long")
elif len1 > len2:
    print(f"{word1} is longer") 
elif len2 > len1:
    print(f"{word2} is longer") 