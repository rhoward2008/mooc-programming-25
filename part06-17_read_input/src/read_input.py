# Write your solution here
def read_input(text, lower, upper):
    while True:
        try:
            number = int(input(text))
            if lower < number < upper:
                return number
        except ValueError:
            pass

        print(f'You must type in an interger between {lower} and {upper}')


if __name__ == '__main__':
    number = read_input('Please type in a number: ',5,10)
    print(f'You typed in: {number}')