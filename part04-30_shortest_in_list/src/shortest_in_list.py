# Write your solution here
def shortest(sentence:list) -> str:
    word = sentence[0]

    for i in sentence:
        if len(i) < len(word):
            word = i
    
    return word


if __name__ == '__main__':
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]
    result = shortest(my_list)
    print(f'Shortest is: {result}')