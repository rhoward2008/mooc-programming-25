from difflib import get_close_matches

PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part07-16_spellchecker_2\\src\\'
file_name = 'wordlist.txt'
words_file = PATH + file_name

words_master = set()



with open(words_file,'r') as dict_file:
    for line in dict_file:
        words_master.add(line.strip().lower())

user_input = input('Write text: ')
sentence = user_input.split(' ')  

suggestions = []

for word in sentence:
    if word.lower() in words_master:
        print(word, end=' ')
    else :
        print(f'*{word}* ', end='')
        suggestions.append([[word],get_close_matches(word,words_master)])

print('\nsuggestions:')

for match in suggestions:
    print(f'{match[0][0]}: {', '.join(match[1])}')