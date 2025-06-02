# Write your solution here
def row_correct(sudoku: list, row_no: int):
    '''Checks if an individual row is valid'''
    num_set = set()
    
    for i in sudoku[row_no]:
        if i in num_set:
            return False
        elif i:
            num_set.add(i)

    return True

def column_correct(sudoku: list, column_no: int):
    '''Checks if an individual column is valid'''
    num_set = set()

    for i in sudoku:
        if i[column_no] in num_set:
            return False
        elif i[column_no]:
            num_set.add(i[column_no])
    
    return True
            
def block_correct(sudoku: list, row_no: int, column_no: int):
    num_set = set()

    for i in sudoku[row_no:row_no+3]:
        for j in i[column_no:column_no+3]:
            if j in num_set:
                return False
            elif j:
                num_set.add(j)

    return True


def sudoku_grid_correct(sudoku: list):
    '''Checks complete sudoku board for validity including rows, columns and grids'''

    #First check all rows
    for i in range(9):
        if not row_correct(sudoku,i):
            return False
    
    #Next check all columns
    for i in range(9):
        if not column_correct(sudoku,i):
            return False
        
    #Next check the 9 sub-blocks
    blocks = [[0,0],[0,3],[0,6],[3,0],[3,3],[3,6],[6,0],[6,3],[6,6]]

    for b in blocks:
        if not block_correct(sudoku,b[0],b[1]):
            return False
    
    #If we have passed all 3 tests, then board is valid
    return True

if __name__ == "__main__":
    sudoku = [
  [2, 6, 7, 8, 3, 9, 5, 0, 4],
  [9, 0, 3, 5, 1, 0, 6, 0, 0],
  [0, 5, 1, 6, 0, 0, 8, 3, 9],
  [5, 1, 9, 0, 4, 6, 3, 2, 8],
  [8, 0, 2, 1, 0, 5, 7, 0, 6],
  [6, 7, 4, 3, 2, 0, 0, 0, 5],
  [0, 0, 0, 4, 5, 7, 2, 6, 3],
  [3, 2, 0, 0, 8, 0, 0, 5, 7],
  [7, 4, 5, 0, 0, 3, 9, 0, 1]
    ]

    
    print(sudoku_grid_correct(sudoku))