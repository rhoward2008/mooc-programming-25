# Write your solution here
folder = 'C:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-write_files\\'
file = 'people.csv'
full_path = folder + file

def store_personal_data(person: tuple):
    with open(full_path,'a') as file_handle:
        new_line = person[0] + ';' + str(person[1]) + ';' + str(person[2])+'\n' 
        file_handle.write(new_line)


if __name__ == '__main__':
    person = 'Paul Paulson',37,175.5
    person2 = 'Eva',23,122
    person3 = 'Bob',33,134.5
    store_personal_data(person)
    store_personal_data(person2)
    store_personal_data(person3)
    print('Program complete')