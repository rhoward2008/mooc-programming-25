# Write your solution here
def row_correct(sudoku: list, row_no: int):
    num_set = set()
    
    for i in sudoku[row_no]:
        if i in num_set:
            return False
        elif i:
            num_set.add(i)

    return True


if __name__ == "__main__":
    sudoku = [
    [9, 1, 2, 7, 8, 4, 3, 6, 5],
    [2, 0, 0, 2, 5, 0, 7, 0, 0],
    [0, 2, 0, 3, 0, 0, 0, 0, 4],
    [2, 9, 4, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 7, 3, 0, 5, 6, 0],
    [7, 0, 5, 0, 6, 0, 4, 0, 0],
    [0, 0, 7, 8, 0, 3, 9, 0, 0],
    [0, 0, 1, 0, 0, 0, 0, 0, 3],
    [3, 0, 0, 0, 0, 0, 0, 0, 2]
    ]
    row = 1
    
    print(row_correct(sudoku,row))