# Write your solution here
def length_of_longest(sentence:list) -> int:
    longest = 0

    for word in sentence:
        if len(word) > longest:
            longest = len(word)
    
    return longest


if __name__ == '__main__':
    #my_list = ['first','second','fourth','eleventhjj']
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = length_of_longest(my_list)
    print(f'longest is: {result}')