# Copy here code of line function from previous exercise
def line(num: int, word: str):
    """Function to print out the first character of a given string x number of times"""
    if len(word) > 0:
        print(word[0]*num)
    else:
        print("*"*num)

def square(size, character):
    for i in range(size):
        line(size, character)

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square(5, "o")