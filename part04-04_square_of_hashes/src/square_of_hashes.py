# Copy here code of line function from previous exercise
def line(num: int, word: str):
    """Function to print out the first character of a given string x number of times"""
    if len(word) > 0:
        print(word[0]*num)
    else:
        print("*"*num)

def square_of_hashes(size):
    for i in range(size):
        line(size, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    square_of_hashes(2)
