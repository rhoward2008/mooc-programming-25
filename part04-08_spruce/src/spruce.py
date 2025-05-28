# Write your solution here
# You can test your function by calling it within the following block
def spruce(size: int):
    """Function to print a spruce tree"""
    print('a spruce!')

    for i in range(1, size+1):
        #print(f'line {i}: {size-i} + {i+i-1} + {size-i}')
        print(' '*(size-i),'*'*(i+i-1),' '*(size-i),sep='')
    
    print(' '*(size-1),'*',sep='')
        




if __name__ == "__main__":
    spruce(6)
 