# Write your solution here
PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-txt_files\\'

file_name = 'recipes1.txt'
full_path = ''

def create_dict(filename: str) -> dict:
    ''' Inputs a filename with multiple recipes.  filename including the full path of the file
    
        Returns a dictionary with one entry per recipe
        example: {'Pancakes: [15, ['milk','eggs']]}

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

def search_by_name(filename:str, word:str) -> list:
    ''' Input name of recipe file and search word
        Output a list of all the recipes names that match the search word
    '''
    found_recipes = []
    recipe_dict = create_dict(filename)
    #print(f'RECIPE dictionary: {recipe_dict}')
    recipe_list = [x for x in recipe_dict.keys()]
    #print(f'JUST NAMES {recipe_list}')
    for recipe in recipe_list:
        if word.lower() in recipe.lower():
            #print(f'Match found: {word} is in {recipe}')
            found_recipes.append(recipe)
    
    #print(f'returning found list: {found_recipes}')
    return found_recipes 

def search_by_time(filename:str, prep_time: int) -> list:
    recipe_dict = create_dict(filename)

    #print(f'seach by time: dict:: {recipe_dict}')
    recipe_time_list = []

    for key,value in recipe_dict.items():
        #print(f'Recipe name: {key}')
        #print(f'Recipe value: {value}')
        if prep_time >= int(value[0]):
            recipe_time_list.append(key + ', preparation time ' + value[0] + ' min')

    #print(recipe_time_list)
    return recipe_time_list

def search_by_ingredient(filename:str, ingredient:str) -> list:
    recipe_dict = create_dict(filename)

    recipe_ing_list = []

    for key,value in recipe_dict.items():
        if ingredient.lower() in value[1]:
            recipe_ing_list.append(key + ', preparation time ' + value[0] + ' min')

    return recipe_ing_list

if __name__ == '__main__':
    
    #name = 'cake'
    #found_recipes = search_by_name(file_name, name)

    #prep_time = 35
    #timed_recipes = search_by_time(file_name, prep_time)

    find_ingredient = 'eggs'
    ingredient_recipes = search_by_ingredient(file_name, find_ingredient)
    
    print(ingredient_recipes)

    