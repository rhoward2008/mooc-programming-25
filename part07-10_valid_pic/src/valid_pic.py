from datetime import datetime
import string

def is_it_valid(pic: str) -> bool:
    '''
    Function to determine if pic is valid.  Must be in format ddmmyyXyyyz

    Return True if valid, else False
    '''

    #First check length, must be 11
    if len(pic) != 11:
        return False
    
    #extract date of birth: day, month
    try:
        day = int(pic[0:2])
        month = int(pic[2:4])
        year = int(pic[4:6])
    except ValueError:
        return False
    
    #find dob year
    century = pic[6]
    if century == '+':
        year = 1800 + year
    elif century == '-':
        year = 1900 + year
    elif century == 'A':
        year = 2000 + year
    else: #Invalid pic, return False
        return False
    
    #Put together dd, mm, yyyy for date of birth
    try:
        dob = datetime(year,month,day)
    except ValueError:
        return False
    
    #print(f'dob: {dob}')

    id = pic[7:10]
    #check that id is valid, must be 3 digits
    for i in id:
        if i not in string.digits:
            return False
    
    control_char = pic[10]
    dividend =  int(pic[0:2] + pic[2:4] + pic[4:6] + id)
    #print(f'numerator: {dividend}')

    #check that control is valid
    remainder = dividend % 31

    lookup = '0123456789ABCDEFHJKLMNPRSTUVWXY'
    if control_char != lookup[remainder]:
        return False

    #print(f'control_char: {control_char}')
    #print(f'lookup: {lookup[remainder]}')
    #print(f'sum: {dividend}')
    #print(f'remainder: {remainder}')
    

    return True

if __name__ == '__main__':
    #pic1 = '230827-906F'
    #pic1 = '120488+246L'
    #pic1 = '310823A9877'
    pic1 = '310899-9877'

    p1 = is_it_valid(pic1)

    if p1:
        print(f'{pic1} is valid')
    else:
        print(f'{pic1} not valid')