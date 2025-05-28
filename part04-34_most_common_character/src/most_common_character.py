# Write your solution here
def most_common_character(word:str) -> str:
    count = 0
    max = ''
    
    for char in word:
        if word.count(char) > count:
            count = word.count(char)
            max = char
    
    return max

if __name__ == '__main__':
    first_string = "exemplaryelementary"
    print(most_common_character(first_string))