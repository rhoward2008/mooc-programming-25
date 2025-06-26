# Write your solution here
def transpose(matrix: list):
    size = len(matrix)
    temp_matrix = [row[:] for row in matrix]

    for x in range(0,size):
        for y in range(0,size):
            matrix[x][y] = temp_matrix[y][x]


if __name__ == '__main__':
    matrix = [[1,2,3],[4,5,6],[7,8,9]]

    print(f'Original: {matrix}')
    transpose(matrix)
    print(f'Updated: {matrix}')