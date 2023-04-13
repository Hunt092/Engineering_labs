def CreateBoard(size):
    return [[" " for i in range(size)] for j in range(size)]


def selectPlayer():

    choice = input("Which Player do you wnt to be: X | O")
    if choice.lower() == "x":
        player, ai = "X", "O"
    elif choice.lower() == "o":
        player, ai = "O", "X"
    else:
        print("Invalid Choice")
        return selectPlayer(player, ai)
    return player, ai


def checkWinner(b):
    for row in range(3):
        if b[row][0] == b[row][1] and b[row][1] == b[row][2]:
            if b[row][0] == player:
                return 10
            elif b[row][0] == ai:
                return -10
    for col in range(3):
        if b[0][col] == b[1][col] and b[1][col] == b[2][col]:

            if b[0][col] == player:
                return 10
            elif b[0][col] == ai:
                return -10

    if b[0][0] == b[1][1] and b[1][1] == b[2][2]:

        if b[0][0] == player:
            return 10
        elif b[0][0] == ai:
            return -10

    if b[0][2] == b[1][1] and b[1][1] == b[2][0]:

        if b[0][2] == player:
            return 10
        elif b[0][2] == ai:
            return -10

    return 0


def isMovesLeft(board):
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                return True
    return False


def minimax(board, depth, isMax):
    score = checkWinner(board)
    if score == 10:
        return score
    if score == -10:
        return score
    if not isMovesLeft(board):
        return 0
    if isMax:
        bestScore = -100000
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == " ":
                    board[i][j] = ai
                    score = minimax(board, depth + 1, False)
                    board[i][j] = ""
                    bestScore = max(bestScore, score)
        return bestScore
    else:
        bestScore = 100000
        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == " ":
                    board[i][j] = player
                    score = minimax(board, depth + 1, True)
                    board[i][j] = ""
                    bestScore = min(bestScore, score)
        return bestScore


def BestMove(board):
    bestScore = -100000
    bestnextMove = ()
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == " ":
                board[i][j] = ai
                score = minimax(board, 0, False)
                board[i][j] = ""
                if score > bestScore:
                    bestnextMove = i, j
                    bestScore = score
    return bestnextMove


def printBoard(board):
    for i in range(len(board)):
        for j in range(len(board)):
            print(f"| {board[i][j]} ", end=" ")
        print("|")


def playGame(board, currentPlayer):
    while isMovesLeft:
        if currentPlayer == player:
            move = list(map(int, (input("Where do ").split(" "))))
            board[move[0]][move[1]] = player
            currentPlayer = ai
        else:
            move = BestMove(board)
            board[move[0]][move[1]] = ai
            currentPlayer = player
        printBoard(board)


if __name__ == "__main__":
    board = CreateBoard(3)
    player, ai = selectPlayer()
    currentPlayer = player
    playGame(board, currentPlayer)
