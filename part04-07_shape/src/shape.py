# Copy here code of line function from previous exercise and use it in your solution
# You can test your function by calling it within the following block
def line(num: int, word: str):
    """Function to print out the first character of a given string x number of times"""
    if len(word) > 0:
        print(word[0]*num)
    else:
        print("*"*num)

def triangle(size: int, char: str):
    # You should call function line here with proper parameters
    for i in range(1, size+1):
        line(i, char)

def shape(triange_size: int, triangle_char: int, height: int, filler: str):
    triangle(triange_size, triangle_char)

    for i in range(height):
        line(triange_size,filler)

    
if __name__ == "__main__":
    shape(3, ".", 0, ",")