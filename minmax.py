import math
from gato import checkWhichMarkWon, checkDraw, board

def minimax(bot, player, board, depth, isMaximizing, alpha=-math.inf, beta=math.inf):
    if (checkWhichMarkWon(bot)):
        return 1, depth
    elif (checkWhichMarkWon(player)):
        return -1, depth
    elif (checkDraw()):
        return 0, depth

    if isMaximizing:
        maxEval = -math.inf
        minDepth = math.inf
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = bot
                eval, evalDepth = minimax(bot, player, board, depth + 1, False, alpha, beta)
                board[key] = ' '
                if eval > maxEval or (eval == maxEval and evalDepth < minDepth):
                    maxEval = eval
                    minDepth = evalDepth
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return maxEval, minDepth

    else:
        minEval = math.inf
        minDepth = math.inf
        for key in board.keys():
            if (board[key] == ' '):
                board[key] = player
                eval, evalDepth = minimax(bot, player, board, depth + 1, True, alpha, beta)
                board[key] = ' '
                if eval < minEval or (eval == minEval and evalDepth < minDepth):
                    minEval = eval
                    minDepth = evalDepth
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return minEval, minDepth


