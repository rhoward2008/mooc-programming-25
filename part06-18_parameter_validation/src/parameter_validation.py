# Write your solution here
def new_person(name: str, age: int):

    if len(name) < 1 or len(name.split(' ')) < 2 or len(name) > 40 or 0 > int(age) or int(age) > 150: 
        raise ValueError('Invalid input')
    person = name,age

    return person

if __name__ == '__main__':
    person = new_person('john doe',280)

    print(person)