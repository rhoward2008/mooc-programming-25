
PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-txt_files\\'

file_name = 'words.txt'
full_path = PATH + file_name

def read_file(word_file: str) -> list:
    '''
    This function reads in a file name with a word list and stores all words in a list
    '''
    word_list = []

    #read the text file and store words in a list
    with open(word_file, 'r') as file_handle:
        for line in file_handle:
            word_list.append(line.strip())

    return word_list


def find_words(search_term: str) -> list:
    '''
    This function inputs a search_term and tries to find it in the text file.
    First read the text file and store all words in a list
    '''
    word_list = read_file(full_path)
    result_list = []

    if '*' in search_term:
        result_list = find_asterix(word_list, search_term)
    elif '.' in search_term:
        result_list = find_dot(word_list, search_term)
    else:
        if search_term in word_list:
            result_list.append(search_term) 
        
    
    return result_list

def find_asterix(word_list:list, search:str) -> list:
    '''
    Input is list of words ie ['cat','dog']
    search term has a * in it to indicate a wildcard of one or more characters 
    '''
    #Match is the list which matches the search term 
    match = []

    for word in word_list:
        
        #Case 1: *abc  Asterix at beginning
        if search[0] == '*':
            #reverse search and remove * in 0 position.  Compare to word reversed 
            #print(f'left: {search[len(search):0:-1]}')
            #print(f'right {word[::-1][:len(search)]}')
            if search[len(search):0:-1] ==  word[::-1][:len(search)-1]:
                match.append(word)
        #Case 2: abc*  Asterix at end
        elif search[-1] == '*':
            #print(f'left: {search[:-1]}')
            #print(f'right: {word[:len(search)-1]} ')
            #compare words, but leave off * at end
            if search[:-1] == word[:len(search)-1]:
                match.append(word)
        #Case 3: ab*c  Asterix in middle
        else:
            #Split into before * and after.  Assume only 1 *
            search_split = search.split('*')
            
            start = search_split[0]
            end = search_split[1]
            #print(f'start: {start}')
            #print(f'end: {end}')

            #Look for a match at the start and end of word
            #print(f'start: {start} :: word:{word[:len(start)]}')
            #print(f'end: {end[::-1]} :: word:{word[::-1][:len(end)]}')
            if start == word[:len(start)] and end[::-1] == word[::-1][:len(end)]:
                match.append(word)

    return match

def find_dot(word_list:str, search:str) -> list:
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
    

    search = 'ba*es'

    answer = find_words(search)

    print(f'Answer: {answer}')

