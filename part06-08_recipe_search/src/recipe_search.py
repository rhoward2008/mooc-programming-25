# Write your solution here
PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-txt_files\\'

file_name = 'recipes1.txt'
full_path = ''

def create_dict(filename: str) -> dict:
    ''' Create dict inputs a filename with multiple recipes and returns a dictionary with one entry per recipe
        example: {'Pancakes: [15, ['milk','eggs']]}

        Input is the filename including the full path of the file
    '''
    full_path = PATH + filename

    #recipe_split is a list that processes the list recipe_list and removes the \n and combines each recipe into a sublist
    recipe_split = []


    with open(full_path, 'r') as recipe_file:
        counter = 0
        name_flag = True
        
        for line in recipe_file:
            if line == '\n':
                counter += 1
                name_flag = True
            elif name_flag:
                recipe_split.append([line.strip()])
                name_flag = False
            else: 
                recipe_split[counter].append(line.strip())

        #print(f'recipe_split')

        recipe_dict = {}

        for single in recipe_split:
            recipe_dict[single[0]] = [single[1],single[2:]]
    
    #print(f'In function: {recipe_dict}')
    return recipe_dict

def search_by_name(filename:str, word:str):
    pass




if __name__ == '__main__':
    new_dict = create_dict(file_name)
    print(f'new_dict: {new_dict}')
    #print('hello')