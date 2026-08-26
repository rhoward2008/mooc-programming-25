import random

def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    '''This function generates random lottery numbers.  All numbers are integers within a given range.
    Numbers cannot be repeated

    parameters:
        amount: The amount of numbers to generate
        lower: The lower limit (inclusive)
        upper: The upper limit (inclusive)
    '''

    all_num = list(range(lower,upper+1))

    results = sorted(random.sample(all_num,amount))

    return results

if __name__ == '__main__':
    
    for number in lottery_numbers(7,1,40):
        print(number)