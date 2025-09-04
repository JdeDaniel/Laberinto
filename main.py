from gato import *
from minmax import *



printBoard(board)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")

def compMove():
    
    bestScore = -math.inf
    bestMove = 0
    
    for key in board.keys():
        if (board[key] == ' '):
            board[key] = bot
            score = minimax(bot, player, board, 0, False)
            board[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key

    insertLetter(bot, bestMove)
    return

def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)
    return

global firstComputerMove
firstComputerMove = True

while not checkForWin():
    compMove()
    playerMove()

