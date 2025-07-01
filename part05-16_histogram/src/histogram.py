# Write your solution here
def histogram(word: str) -> None:
    '''Function takes a string as input and creates a dictionary which contains 
        a count of each letter in the string.  Next print out a histogram of the 
        occurences of each letter'''
    word_dict = {}
    for letter in word:
        if letter not in word_dict:
            word_dict[letter] = 0
        
        word_dict[letter] += 1
    
    for key,value in word_dict.items():
        print(key, end=' ')
        print('*'*value)
    


if __name__ == '__main__':
    word1 = 'statistically'
    histogram(word1)