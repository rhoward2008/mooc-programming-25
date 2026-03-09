import random, string

def generate_password(length: int):
    password = ''

    for i in range(length):
        password += string.ascii_lowercase[random.randint(0,25)]
    
    return password


if __name__ == '__main__':
    
    for i in range(10):
        print(generate_password(8))
