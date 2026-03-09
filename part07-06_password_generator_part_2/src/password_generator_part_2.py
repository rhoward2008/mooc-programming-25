import random, string

def generate_strong_password(length: int, include_numbers: bool, include_special: bool):
    '''
    Function to generate a pseudo random password

    Arguments:
        length: The length of the password
        numbers: A boolean to indicate if numbers should be included
        special: A boolean to indicate if special characters should be included
    
    Returns: string of the generate password
    '''
    password = [] #Store the password as a list, later convert to string
    pool_of_chars = string.ascii_lowercase

    #The password must always contain at least one lower case letter
    password.append(pool_of_chars[random.randint(0,25)])

    #If 2nd param is true, add the digits to the available pool of characters
    if include_numbers:
        pool_of_chars +=  string.digits
    
    #If 3rd param is true, ddd special characters
    if include_special:
        pool_of_chars += '!?=+-()#'

    for i in range(length-1):
        password.append(random.choice(pool_of_chars))
    
    random.shuffle(password)
    shuffled_pw = "".join(password)

    return shuffled_pw


if __name__ == '__main__':
    
    for i in range(10):
        print(generate_strong_password(8, True, True))
