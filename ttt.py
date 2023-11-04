from math import inf 

global prune 
global counter
counter = 0
prune = True
humanCheck = -1
compCheck = +1
board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
]


def currCheck(curr):

    if checkWinner(curr, compCheck):
        curr_score = +1
    elif checkWinner(curr, humanCheck):
        curr_score = -1
    else:
        curr_score = 0

    return curr_score

def checkWinner(curr, player):
    # checks for winner in game

    # Check rows
    for i in range(3):
        if curr[i][0] == curr[i][1] == curr[i][2] == player:
            return True

    # Check columns
    for j in range(3):
        if curr[0][j] == curr[1][j] == curr[2][j] == player:
            return True

    # Check diagonals
    if curr[0][0] == curr[1][1] == curr[2][2] == player:
        return True
    if curr[0][2] == curr[1][1] == curr[2][0] == player:
        return True

    # No win condition met
    return False

def gameCheck(curr):
    return checkWinner(curr, humanCheck) or checkWinner(curr, compCheck)

def usableSpace(curr):

    return [[x, y] for x, row in enumerate(curr) for y, cell in enumerate(row) if cell == 0]

def reset_board():
    global board

    board = [
    [0, 0, 0],
    [0, 0, 0],
    [0, 0, 0],
    ]

    return board

def makeMoveForce(x, y, player):

    board[x][y] = player
    return True

def minimax(currBoard, boardDepth, player, prune, alpha=-float('inf'), beta=float('inf'), recur = False):
    global counter
    counter += 1
    reoccurCheck = 0
    # print("check", recur)
    if boardDepth == 0 or gameCheck(currBoard):
        currScore = currCheck(currBoard)
        return [-1, -1, currScore]

    if player == compCheck:
        # currScore = maxscore(currBoard, boardDepth - 1, -player, prune, alpha, beta)
        maxVal = [-1, -1, -float('inf')]
        for currSpace in usableSpace(currBoard):
            x, y = currSpace
            currBoard[x][y] = player

            # print()
            # print("currCheck X", x)
            # print("currCheck Y", y)
            # print()
            currScore = minimax(currBoard, boardDepth - 1, -player, prune, alpha, beta, True)
            currBoard[x][y] = 0
            currScore[0], currScore[1] = x, y

            if (recur == False):
                # if currScore[2] == 0:
                #     continue
                # elif currScore[2] == 1:
                #     currScore[2] = 1 - .1 * boardDepth
                # elif currScore[2] == -1:
                #     currScore[2] = -1 + .1 * boardDepth
                transcript(x, y, currScore[2])
            
            if currScore[2] > maxVal[2]:
                
                maxVal = currScore  # max value
                
            if prune:
                alpha = max(alpha, maxVal[2])
                if beta <= alpha:
                    break

    else:
        # currScore = minscore(currBoard, boardDepth - 1, -player, prune, alpha, beta)
        maxVal = [-1, -1, float('inf')]
        for currSpace in usableSpace(currBoard):
            x, y = currSpace
            currBoard[x][y] = player
            currScore = minimax(currBoard, boardDepth - 1, -player, prune, alpha, beta, True)
            currBoard[x][y] = 0
            currScore[0], currScore[1] = x, y

            if (recur == False):
                # print("e")
                # if currScore[2] == 0:
                #     continue
                # elif currScore[2] == 1:
                #     currScore[2] = 1 - .1 * boardDepth
                # elif currScore[2] == -1:
                #     currScore[2] = -1 + .1 * boardDepth
                transcript(x, y, currScore[2])
            if currScore[2] < maxVal[2]:
                maxVal = currScore  # min value


            if prune:
                beta = min(beta, maxVal[2])
                if beta <= alpha:
                    break

    return maxVal

def transcript(x, y, score):
    if (x == 0):
        x = "A"
    elif (x == 1):
        x = "B"
    elif (x == 2):
        x = "C"

    y += 1

    score = float(score)

    print("move (",x, ",", y,") mm-score: ", score)


def minscore(currBoard, boardDepth, player, prune, alpha=-float('inf'), beta=float('inf'), recur = False):
    global counter
    counter += 1
    if boardDepth == 0 or gameCheck(currBoard):
        currScore = currCheck(currBoard)
        return [-1, -1, currScore]
    minVal = [-1, -1, float('inf')]
    for currSpace in usableSpace(currBoard):
        x, y = currSpace
        currBoard[x][y] = player
        currScore = minimax(currBoard, boardDepth - 1, -player, prune, alpha, beta, True)
        currBoard[x][y] = 0
        currScore[0], currScore[1] = x, y

        if (recur == False):
            # print("e")
            # if currScore[2] == 0:
            #     continue
            # elif currScore[2] == 1:
            #     currScore[2] = 1 - .1 * boardDepth
            # elif currScore[2] == -1:
            #     currScore[2] = -1 + .1 * boardDepth
            transcript(x, y, currScore[2])
        if currScore[2] < minVal[2]:
            minVal = currScore  # min value


        if prune:
            beta = min(beta, minVal[2])
            if beta <= alpha:
                break

    return minVal

def maxscore(currBoard, boardDepth, player, prune, alpha=-float('inf'), beta=float('inf'), recur = False):
    global counter
    counter += 1
    if boardDepth == 0 or gameCheck(currBoard):
        currScore = currCheck(currBoard)
        return [-1, -1, currScore]
    maxVal = [-1, -1, -float('inf')]
    for currSpace in usableSpace(currBoard):
        x, y = currSpace
        currBoard[x][y] = player

        # print()
        # print("currCheck X", x)
        # print("currCheck Y", y)
        # print()
        currScore = minimax(currBoard, boardDepth - 1, -player, prune, alpha, beta, True)
        currBoard[x][y] = 0
        currScore[0], currScore[1] = x, y

        if (recur == False):
            # if currScore[2] == 0:
            #     continue
            # elif currScore[2] == 1:
            #     currScore[2] = 1 - .1 * boardDepth
            # elif currScore[2] == -1:
            #     currScore[2] = -1 + .1 * boardDepth
            transcript(x, y, currScore[2])
        
        if currScore[2] > maxVal[2]:
            
            maxVal = currScore  # max value
            
        if prune:
            alpha = max(alpha, maxVal[2])
            if beta <= alpha:
                break
    
    return maxVal

def printBoard(currBoard, compTurn, humanTurn):

    print()
    for row in currBoard:
        for space in row:
            if space == -1:
                currPiece = humanTurn
            elif space == +1: 
                currPiece = compTurn
            else:
                currPiece = '.'
            print(f' {currPiece} ', end='')
        print()

def comp_turn(compTurn, humanTurn, prune):
    global counter
    boardDepth = len(usableSpace(board))

    # printBoard(board, compTurn, humanTurn)

    compMove = minimax(board, boardDepth, compCheck, prune)
    # print("move", compMove)
    print("number of nodes searched:", counter)
    counter = 0
    row, col = compMove[0], compMove[1]

    makeMoveForce(row, col, compCheck)
    printBoard(board, compTurn, humanTurn)
    print()

def playerComp_turn(humanTurn, compTurn, prune):
    global counter
    boardDepth = len(usableSpace(board))

    # printBoard(board, compTurn, humanTurn)

    playerMove = minimax(board, boardDepth, humanCheck, prune)
    # print("move", playerMove)
    print("number of nodes searched:", counter)

    counter = 0
    row, col = playerMove[0], playerMove[1]

    makeMoveForce(row, col, humanCheck)
    printBoard(board, compTurn, humanTurn)
    print()

def player_turn(compTurn, humanTurn):

    global prune
    nextTurn = False

    while (nextTurn != True):
        move = input('Make your move: ')
        inputSplit = move.split()
        if (move == "choose X" or move == "choose x"):
            # print("brb")
            playerComp_turn(humanTurn, compTurn, prune)
            break
        elif (move == "choose O" or move == "choose o"):
            comp_turn(compTurn, humanTurn, prune)
            break
            
        elif (move == "show"):
            # printBoard(board, compTurn, humanTurn)
            move = input('Make your move: ')

        elif (move == "reset"):
            clear_board = reset_board()
            printBoard(clear_board, compTurn, humanTurn)
            # move = input('Make your move: ')
            break
        elif (move == "quit"):
            exit()
        elif (move == "pruning"):
            if (prune == True):
                print("The current curr of pruning is on.")
            else:
                print("The current curr of pruning is off.")
                
        elif (inputSplit[0] == "pruning"):
                if (inputSplit[1] == "off"):
                    prune = False
                    print("The current curr of pruning is off.")
                else: 
                    prune = True
                    print("The current curr of pruning is on.")
            
        elif(inputSplit[0] == "move"):
            # move P R C
            print(inputSplit[2])
            if (inputSplit[2] == 'A' or inputSplit[2] == 'a'):
                curr_move = 0 
            elif (inputSplit[2] == 'B' or inputSplit[2] == 'b'):
                curr_move = 1 
            elif (inputSplit[2] == 'C' or inputSplit[2] == 'c'):
                curr_move = 2 

            y = int(inputSplit[3]) - 1
            if (inputSplit[1] == 'X' or inputSplit[1] == 'x'):
                makeMoveForce(curr_move, y, humanCheck)
                printBoard(board, compTurn, humanTurn)
            else:
                makeMoveForce(curr_move, y, compCheck)
                printBoard(board, compTurn, humanTurn)
            break
                
        # printBoard(board, compTurn, humanTurn)
        # move = input('Make your move: ')
            

def main():

    humanTurn = 'X'  
    compTurn = 'O' 
    gameCont = False
    print()
    print("Welcome to Tic-Tac-Toe")
    print()
    while True:
        if ((len(usableSpace(board)) > 0) and not gameCheck(board)):
            gameCont = True
        else: 
            gameCont = False
            break

        while gameCont:     

            player_turn(compTurn, humanTurn)
            break

    if checkWinner(board, humanCheck):
        print(f'{humanTurn} won!')
    elif checkWinner(board, compCheck):
        print(f'{compTurn} won!')
    else:
        print('Tie!')

    # print("Number of nodes traversed:", counter)

    exit()


if __name__ == '__main__':
    main()