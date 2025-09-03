import numpy as np

def max_valor(game, state, alpha=float('-inf'), beta=float('inf')):
    """
    Valores de los movimientos de Max
    """
    if game.is_terminal(state):
        #Si el estado es terminal, devolvemos el valor del juego
        return game.utility(state), None
    
    # Inicializamos el valor máximo como negativo infinito
    max_value = float('-inf')
    for action in game.actions(state):
        next_state = game.result(state, action)
        value = min_valor(game, next_state, alpha, beta)
        max_value = max(max_value, value)
        alpha = max(alpha, max_value)
        if beta <= alpha:
            break # Poda
    
    return max_value, action

def min_valor(game, state, alpha=float('-inf'), beta=float('inf')):
    """
    Valores de los movimientos de Min
    """
    if game.is_terminal(state):
        #Si el estado es terminal, devolvemos el valor del juego
        return game.utility(state), None
    
    # Inicializamos el valor mínimo como positivo infinito
    min_value = float('inf')
    for action in game.actions(state):
        next_state = game.result(state, action)
        value = max_valor(game, next_state, alpha, beta)
        min_value = min(min_value, value)
        beta = min(beta, min_value)
        if beta <= alpha:
            break # Poda
    
    return min_value, action

def minimax(game):
    """
    Algoritmo Minimax con poda Alpha-Beta
    """
    state = game.initial_state()
    jugadas = []
    value, move = max_valor(game, state)
    while True:
        