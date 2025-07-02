# Write your solution here
def invert(dictionary: dict):
    all_keys = []
    for key,value in list(dictionary.items()):
        dictionary[value] = key
        del dictionary[key]
    
    #print(f'In function: {dictionary}')

if __name__ == '__main__':
    my_dict = {1: 'first', 2: 'second' }

    invert(my_dict)
    print(f'Inverted dictionary: {my_dict}')