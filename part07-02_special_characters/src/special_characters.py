import string

def separate_characters(my_string: str) -> list:
    parts = ['','','']
    
    for char in my_string:
        
        if char in string.ascii_letters:
            parts[0] += char
        
        elif char in string.punctuation:
            parts[1] += char
        
        else:
            parts[2] += char
    
    
    return parts

if __name__ == '__main__':
    my_string = 'Olé!!! Hey, are ümläüts wörking?'
    parts = separate_characters(my_string)

    print(parts[0])
    print(parts[1])
    print(parts[2])