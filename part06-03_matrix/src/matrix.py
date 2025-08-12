# write your solution here
PATH = 'c:\\Users\\bension.dworkin\\github_repo\\mooc-programming-25\\part06-txt_files\\'
full_path = PATH + 'matrix.txt'

def matrix_sum():
    with open(full_path,'r') as new_file:
        total = 0

        for row in new_file:
            total += list_sum(row)
        
        return total

def matrix_max():
    with open(full_path,'r') as new_file:
        max_list = [] 

        for row in new_file:
            num_list = sorted([int(x) for x in row.split(',')])
            #print(f'NumList: {num_list}')
            max_list.append(num_list[-1])
            
        max_list.sort()
        #print(f'Max list: {max_list}')

        return max_list[-1]
        

def row_sums():
    with open(full_path,'r') as new_file:
        sum_list = []

        for row in new_file:
            sum_list.append(list_sum(row))
        
        return sum_list

def list_sum(line):
    ''' Inputs a line from the matrix in string format.  
        Splits it into a list, converts to an int and returns the sum
    '''
    num_list = line.split(',')
    sum = 0
    for i in num_list:
        sum += int(i)
    
    return sum

if __name__ == '__main__':
    sum = matrix_sum()
    max = matrix_max()
    row = row_sums()
    print(f'Sum of matrix = {sum}') 
    print(f'Max of matrix = {max}') 
    print(f'List of sums = {row}') 
