# Copy here code of line function from previous exercise
def line(num: int, word: str):
    """Function to print out the first character of a given string x number of times"""
    if len(word) > 0:
        print(word[0]*num)
    else:
        print("*"*num)

def triangle(size):
    # You should call function line here with proper parameters
    for i in range(1, size+1):
        line(i, "#")

# You can test your function by calling it within the following block
if __name__ == "__main__":
    triangle(6)
