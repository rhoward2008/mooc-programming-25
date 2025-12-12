# write your solution here
PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-txt_files\\'
full_path = PATH + 'fruits.csv'

def read_fruits():
    fruit_dict = {}

    #with open('fruits.csv','r') as new_file:
    with open(full_path,'r') as new_file:
        for line in new_file:
            line = line.replace('\n','').split(';')

            fruit_dict[line[0]] = float(line[1])
    
    return fruit_dict

if __name__ == '__main__':
    fruits = read_fruits()
    print(fruits)


