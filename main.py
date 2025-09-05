from gato import *
from minmax import *

imprimeTablero(tablero)
print("Bienvenido al juego de gato")
print("Tu eres 'O' y la computadora es 'X'")
print("Para hacer una jugada, elige un numero del 1 al 9")
print("El tablero es asi:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("X empieza primero, buena suerte")
print("\n")
    
def compMove():
    mejorPuntaje = -math.inf
    mejorMovimiento = None
    mejorProfundidad = math.inf

    for lugar in tablero.keys():
        if tablero[lugar] == ' ':
            tablero[lugar] = bot
            puntaje, profundidad = minimax(bot, jugador, tablero, 0, False)
            tablero[lugar] = ' '
            # Si el puntaje es mejor, o igual pero gana más rápido
            if (puntaje > mejorPuntaje) or (puntaje == mejorPuntaje and profundidad < mejorProfundidad):
                mejorPuntaje = puntaje
                mejorMovimiento = lugar
                mejorProfundidad = profundidad

    if mejorMovimiento is not None:
        ingresoJugada(bot, mejorMovimiento)
    return

def movimientoJugador():
    posicion = int(input("Ingrese posicion para 'O':  "))
    ingresoJugada(jugador, posicion)
    return

global firstComputerMove
firstComputerMove = True

while not revisaGanador():
    compMove()
    movimientoJugador()

