import math
from gato import checkWhichMarkWon, checkDraw, board



def minimax(bot, player, board, depth, isMaximizing):
    alpha = -math.inf
    beta = math.inf
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                tempAlpha = minimax(bot, player, board, depth + 1, False)
                board[key] = ' '
                if (tempAlpha > alpha):
                    alpha = tempAlpha
        return alpha

    else:
        bestScore = math.inf #beta
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                score = minimax(bot, player, board, depth + 1, True)
                board[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


