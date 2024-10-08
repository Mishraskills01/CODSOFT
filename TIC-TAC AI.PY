import random

# The game board
board = [' ' for _ in range(9)]

# Function to insert a letter at a specific position on the board
def insertLetter(letter, pos):
    board[pos] = letter

# Function to check if a space on the board is free
def spaceIsFree(pos):
    return board[pos] == ' '

# Function to print the current state of the board
def printBoard(board):
    print(' ' + board[0] + ' | ' + board[1] + ' | ' + board[2])
    print('-----------')
    print(' ' + board[3] + ' | ' + board[4] + ' | ' + board[5])
    print('-----------')
    print(' ' + board[6] + ' | ' + board[7] + ' | ' + board[8])

# Function to check if the board is full
def isBoardFull(board):
    return board.count(' ') == 0

# Function to check for a win
def isWinner(b, l):
    return ((b[0] == l and b[1] == l and b[2] == l) or
            (b[3] == l and b[4] == l and b[5] == l) or
            (b[6] == l and b[7] == l and b[8] == l) or
            (b[0] == l and b[3] == l and b[6] == l) or
            (b[1] == l and b[4] == l and b[7] == l) or
            (b[2] == l and b[5] == l and b[8] == l) or
            (b[0] == l and b[4] == l and b[8] == l) or
            (b[2] == l and b[4] == l and b[6] == l))

# Function to handle player move
def playerMove():
    run = True
    while run:
        move = input('Please select a position to place an \'X\' (1-9): ')
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move-1):
                    run = False
                    insertLetter('X', move-1)
                else:
                    print('Sorry, this space is occupied!')
            else:
                print('Please type a number within the range!')
        except:
            print('Please type a number!')

# Function to handle computer move
def compMove():
    bestScore = -1000
    bestMove = 0
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            score = minimax(board, 0, False)
            board[i] = ' '
            if score > bestScore:
                bestScore = score
                bestMove = i
    insertLetter('O', bestMove)
    return

# Minimax function
def minimax(board, depth, isMaximizing):
    if isWinner(board, 'O'):
        return 10
    elif isWinner(board, 'X'):
        return -10
    elif isBoardFull(board):
        return 0

    if isMaximizing:
        bestScore = -1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, depth + 1, False)
                board[i] = ' '
                bestScore = max(score, bestScore)
        return bestScore
    else:
        bestScore = 1000
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, depth + 1, True)
                board[i] = ' '
                bestScore = min(score, bestScore)
        return bestScore

# Main function
def main():
    print('Welcome to Tic Tac Toe!')
    printBoard(board)

    while not(isBoardFull(board)):
        if not(isWinner(board, 'O')):
            playerMove()
            printBoard(board)
        else:
            print('Sorry, O\'s won this time!')
            break

        if not(isWinner(board, 'X')):
            compMove()
            printBoard(board)
        else:
            print('X\'s won this time! Good Job!')
            break

    if isBoardFull(board):
        print('Tie Game!')

main()