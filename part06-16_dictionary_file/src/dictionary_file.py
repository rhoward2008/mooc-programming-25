
PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-write_files\\'

file_name = 'dictionary.txt'
full_path = PATH + file_name


def add_words():
    '''
    This function adds words to the dictionary text file.
    '''
    word_finnish = input('The word in Finnish: ')
    word_english = input('The word in Englist: ')

    with open(full_path ,'a') as dict_file:
        dict_file.write(f'{word_finnish};{word_english}\n')

def search_words():
    '''
    This function asks for an input search term, reads the dictionary text files and searches for any matches in the dictionary.
    '''
    search_term = input('Search term: ')

    #First read the file and save into word_dict
    #Assume file is csv with semi-colon delimeter
    word_dict = {}

    #Store all matches in a dictionary
    result_dict = {}

    try:
        with open(full_path, 'r') as dict_file:
            for line in dict_file:
                new_word = line.strip().split(';')
                word_dict[new_word[0]] = new_word[1]
    except FileNotFoundError:
        print('Dictionary is empty.')

    #loop through dictionary and check if each entry is a match
    #If yes add to result dict
    for key,value in word_dict.items():
        #print(f'key: {key}, value: {value}')
        if is_match(search_term, (key,value)):
            result_dict[key] = value
    
    #Print all matching results
    for key,value in result_dict.items():
        print(f'{key} - {value}')

def is_match(search_word:str, word_pair:tuple) -> bool:
    '''
    Take search term and checks if there is a match with the word_pair tuple.  Tuple has Finnish word and English word pair.
    '''
    # Case 1 match at start of word 
    # abc*
    if word_pair[0].startswith(search_word) or word_pair[1].startswith(search_word):
        return True
    # Case 2 match at end of word
    # *abc
    elif word_pair[0].endswith(search_word) or word_pair[1].endswith(search_word):
        return True
    # Case 3 match in middle of word
    elif search_word in word_pair[0] or search_word in word_pair[1]:
        return True
    else:
        return False
    



while True:
    user_input = input('1 - Add word, 2 - Search, 3 - Quit\nFunction: ')

    if user_input == '1':
        add_words()
    elif user_input == '2':
        search_words()
    elif user_input == '3':
        print('Goodbye!')
        break
    else:
        print('Invalid input')