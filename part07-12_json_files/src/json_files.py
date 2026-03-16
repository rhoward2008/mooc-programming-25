import json

PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part07-12_json_files\\src\\'


def print_person(filename: str):
    with open(filename) as file_handle:
        file_data = file_handle.read()

    person_list = json.loads(file_data)
    #print(person_list)

    for person in person_list:
        print(f'{person['name']} {person['age']} years ',end='')
        print('(' + ', '.join(person['hobbies']) + ')')

if __name__ == '__main__':
    file_name = 'person.json'
    full_file = PATH + file_name
    print_person(full_file)