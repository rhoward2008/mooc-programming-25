def chessboard(num):
    line = ''
    line2 = ''
    for i in range(num):
        line += str((i+1)%2)
        line2 += str((i) % 2)

    for i in range(num):
        if (i+1)%2:
            print(line)
        else:
            print(line2)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    chessboard(3)

