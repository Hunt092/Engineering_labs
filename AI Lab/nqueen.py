def create_board(size):
    board = [[0 for j in range(size)] for i in range(size)]
    return board


def checkCol(board, row, col):
    for i in range(col):
        if board[row][i] == 1:
            return False
    return True


def checkDiagonals(board, row, col):
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    for i, j in zip(range(row, size, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def isClear(board, row, column):
    return checkCol(board, row, column) & checkDiagonals(board, row, column)


def placeQueen(board, col):
    if col >= size:
        return True
    for i in range(size):
        if isClear(board, i, col):
            board[i][col] = 1
            if placeQueen(board, col + 1):
                return True
            else:
                board[i][col] = 0

    return False


def printBoard(board):
    for i in range(size):
        for j in range(size):
            print(board[i][j], end=" ")
        print("")


if __name__ == "__main__":
    size = int(input("What is the size of board: \n"))
    board = create_board(size)
    if placeQueen(board, 0):
        printBoard(board)
    else:
        print("No Solution exists")
