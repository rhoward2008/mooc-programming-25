# write your solution here
PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-txt_files\\'
file_name = 'wordlist.txt'
words_file = PATH + file_name

words_master = set()



with open(words_file,'r') as dict_file:
    for line in dict_file:
        words_master.add(line.strip().lower())

user_input = input('Write text: ')
sentence = user_input.split(' ')  

for word in sentence:
    if word.lower() in words_master:
        print(word, end=' ')
    else :
        print(f'*{word}* ', end='')