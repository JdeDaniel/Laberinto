import math
from gato import revisaQuien, empate, tablero

def minimax(bot, jugador, tablero, profundidad, isMaximizing, alpha=-math.inf, beta=math.inf):
    if (revisaQuien(bot)):
        return 1, profundidad
    elif (revisaQuien(jugador)):
        return -1, profundidad
    elif (empate()):
        return 0, profundidad

    if isMaximizing:
        maxEval = -math.inf
        minprofundidad = math.inf
        for lugar in tablero.keys():
            if (tablero[lugar] == ' '):
                tablero[lugar] = bot
                eval, evalprofundidad = minimax(bot, jugador, tablero, profundidad + 1, False, alpha, beta)
                tablero[lugar] = ' '
                if eval > maxEval or (eval == maxEval and evalprofundidad < minprofundidad):
                    maxEval = eval
                    minprofundidad = evalprofundidad
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return maxEval, minprofundidad

    else:
        minEval = math.inf
        minprofundidad = math.inf
        for lugar in tablero.keys():
            if (tablero[lugar] == ' '):
                tablero[lugar] = jugador
                eval, evalprofundidad = minimax(bot, jugador, tablero, profundidad + 1, True, alpha, beta)
                tablero[lugar] = ' '
                if eval < minEval or (eval == minEval and evalprofundidad < minprofundidad):
                    minEval = eval
                    minprofundidad = evalprofundidad
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return minEval, minprofundidad


