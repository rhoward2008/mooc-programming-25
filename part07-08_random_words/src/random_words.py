import random
input_file = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part07-08_random_words\\src\\words.txt'

def words(n: int, beginning: str) -> list:
    word_list = []

    with open(input_file, 'r') as file_handle:
        for line in file_handle:
            word = line.strip()
            if word.startswith(beginning) and word not in word_list:
                word_list.append(word)

    #print(f'word_list: {word_list}')
    if len(word_list) < n:
        raise ValueError
    
    return random.sample(word_list,n)

if __name__ == '__main__':
    search = 'alo'
    word_list = words(3, search)
    #print(f'word list: {word_list}')
    for word in word_list:
        print(word)