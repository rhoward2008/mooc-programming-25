# Write your solution here
def print_sudoku(sudoku:list):
    for row in sudoku:
        for col in range(0,len(row)):
            if col%3 == 0:
                print(' ',end='')
            if row[col]:
                print(row[col],end='')
            else:
                print('_',end='')
        
        print('\n')
        
def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
    new_sudoku = [row[:] for row in sudoku]
    new_sudoku[row_no][column_no] = number
    return new_sudoku

if __name__ == "__main__":
    sudoku  = [
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]
    grid_copy = copy_and_add(sudoku, 0, 0, 2)
    print("Original:")
    print_sudoku(sudoku)
    print()
    print("Copy:")
    print_sudoku(grid_copy)
