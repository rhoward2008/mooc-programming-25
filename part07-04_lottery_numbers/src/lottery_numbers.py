import random

def lottery_numbers(amount: int, lower: int, upper: int) -> list:
    results =[]
    for x in range(1,amount+1):
        results.append(random.randint(lower,upper))

    return results

if __name__ == '__main__':

    for number in lottery_numbers(7,1,40):
        print(number)