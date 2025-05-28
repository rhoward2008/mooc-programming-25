# Write your solution here
def all_the_longest(sentence:list) -> list:
    ''' Function to take a list of strings and return a new list
        with the longest string in the orignal list.  If there is a tie,
        return all longest in the orignal order'''
    longest = 0
    new_list = []

    for word in sentence:
        if len(word) == longest:
            new_list.append(word)
        elif len(word) > longest:
            longest = len(word)
            new_list = [word]
    
    return new_list



if __name__ == '__main__':
    my_list = ["adele", "mark", "dorothy", "tim", "hedy", "richard"]

    result = all_the_longest(my_list)
    print(result) # ['eleventh']