
PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-txt_files\\'

file_name = 'words.txt'
full_path = PATH + file_name



def find_word(search_term: str) -> list:
    '''
    This function inputs a search_term and tries to find it in the text file.
    First read the text file and store all words in a list
    '''
    word_list = []
    result_list = []

    #read the text file and store words in a list
    with open(full_path, 'r') as file_handle:
        for line in file_handle:
            word_list.append(line.strip())

    if '*' in search_term:
        result_list = find_asterix()
    elif '.' in search_term:
        result_list = find_dot(word_list, search_term)
    else:
        if search_term in word_list:
            result_list.append(search_term) 
        
    
    return result_list

def find_asterix(word_list, search):
    '''
    Input is list of words ie ['cat','dog']
    search term has a * in it to indicate a wildcard of one or more characters 
    '''
    #Match is the list which matches the search term 
    match = []

    for word in word_list:
        pass

    return match

def find_dot(word_list, search):
    '''
    Input is list of words ie ['cat','dog']
    search term has a . in it to indicate a single character '.at' or 'c.t'
    '''
    #Match is the list which matches the search term 
    match = []

    for word in word_list:
        word_length = len(word)
        counter = 0

        #Search word and comparison word must be the same length otherwise there is no match
        #If length is different, move on to the next word in the list
        if word_length == len(search): 

            #Check that all letters in the word match.  A dot . is a singleton wildcard
            for i,letter in enumerate(word):
                #print(f'{i}: {letter}')
                if letter == search[i] or search[i] == '.':
                    counter += 1

            if word_length == counter:
                match.append(word)

    #print(f'match_list: {match}')

    return match

if __name__ == '__main__':
    
    #search = '.at'

    test = ['dog','cat','hat']

    answer = find_word(test,search)

    print(f'Answer: {answer}')


    #answer = find_word(search)
    #print(f'Search term is: {search}.  \nResults are: {answer}')
