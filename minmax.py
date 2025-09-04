import math
from gato import checkWhichMarkWon, checkDraw, board

def minimax(bot, player, board, depth, isMaximizing, alpha=-math.inf, beta=math.inf):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        maxEval = -math.inf
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                eval = minimax(bot, player, board, depth + 1, False, alpha, beta)
                board[key] = ' '
                maxEval = max(maxEval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    #print("Alpha: " + str(alpha) + " Beta: " + str(beta))
                    break
        return maxEval

    else:
        minEval = math.inf
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                eval = minimax(bot, player, board, depth + 1, True, alpha, beta)
                board[key] = ' '
                minEval = min(minEval, eval)
                beta = min(beta, eval)
                if beta >= alpha:
                    #print("Alpha: " + str(alpha) + " Beta: " + str(beta))
                    break
        return minEval


