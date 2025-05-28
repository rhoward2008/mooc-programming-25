# Write your solution here
def squared(word,num):
    pointer = 0
    word_length = len(word)
    for i in range(num):
        for j in range(num):
            #print(f'Char: {pointer%)
            #print(f'Char: {word[pointer%word_length]}')
            print(word[pointer%word_length],end="")
            pointer += 1
        print('\n',end="")


# You can test your function by calling it within the following block
if __name__ == "__main__":
    squared('aybabtu',5)
