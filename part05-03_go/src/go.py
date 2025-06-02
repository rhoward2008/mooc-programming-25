# Write your solution here
def who_won(game_board: list):
    player1 = 0
    player2 = 0
    winner = 0

    for i in game_board:
        for j in i:
            if j == 1:
                player1 += 1
            elif j == 2:
                player2 += 1

    if player1 > player2:
        winner = 1
    elif player2 > player1:
        winner = 2
        
    return winner

if __name__ == "__main__":
    board = [[1, 2, 2], [0, 1, 2], [2, 0, 1]] 
    result = who_won(board)
    print(f'Result is {result}')