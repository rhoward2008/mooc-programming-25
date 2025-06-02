# Write your solution here
def column_correct(sudoku: list, column_no: int):
    num_set = set()

    for i in sudoku:
        if i[column_no] in num_set:
            return False
        elif i[column_no]:
            num_set.add(i[column_no])
    
    return True
            

if __name__ == "__main__":
    sudoku = [
    [9, 1, 2, 7, 8, 4, 3, 6, 5],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 2],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    row = 3
    
    print(column_correct(sudoku,row))