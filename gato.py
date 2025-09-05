jugador = 'O'
bot = 'X'

def imprimeTablero(tablero):
    print(tablero[1] + '|' + tablero[2] + '|' + tablero[3])
    print('-+-+-')
    print(tablero[4] + '|' + tablero[5] + '|' + tablero[6])
    print('-+-+-')
    print(tablero[7] + '|' + tablero[8] + '|' + tablero[9])
    print("\n")

def espacioDisponible(posicion):
    if tablero[posicion] == ' ':
        return True
    else:
        return False

def ingresoJugada(letra, posicion):
    if espacioDisponible(posicion):
        tablero[posicion] = letra
        imprimeTablero(tablero)
        if (empate()):
            print("Empate")
            exit()
        if revisaGanador():
            if letra == 'X':
                print("Gana la computadora")
                exit()
            else:
                print("Jugador gana")
                exit()
        return
    else:
        print("Jugada no valida")
        posicion = int(input("Porfavor elige otro espacio:  "))
        ingresoJugada(letra, posicion)
        return
    
def revisaGanador():
    if (tablero[1] == tablero[2] and tablero[1] == tablero[3] and tablero[1] != ' '):
        return True
    elif (tablero[4] == tablero[5] and tablero[4] == tablero[6] and tablero[4] != ' '):
        return True
    elif (tablero[7] == tablero[8] and tablero[7] == tablero[9] and tablero[7] != ' '):
        return True
    elif (tablero[1] == tablero[4] and tablero[1] == tablero[7] and tablero[1] != ' '):
        return True
    elif (tablero[2] == tablero[5] and tablero[2] == tablero[8] and tablero[2] != ' '):
        return True
    elif (tablero[3] == tablero[6] and tablero[3] == tablero[9] and tablero[3] != ' '):
        return True
    elif (tablero[1] == tablero[5] and tablero[1] == tablero[9] and tablero[1] != ' '):
        return True
    elif (tablero[7] == tablero[5] and tablero[7] == tablero[3] and tablero[7] != ' '):
        return True
    else:
        return False

def revisaQuien(mark): 
    if tablero[1] == tablero[2] and tablero[1] == tablero[3] and tablero[1] == mark:
        return True
    elif (tablero[4] == tablero[5] and tablero[4] == tablero[6] and tablero[4] == mark):
        return True
    elif (tablero[7] == tablero[8] and tablero[7] == tablero[9] and tablero[7] == mark):
        return True
    elif (tablero[1] == tablero[4] and tablero[1] == tablero[7] and tablero[1] == mark):
        return True
    elif (tablero[2] == tablero[5] and tablero[2] == tablero[8] and tablero[2] == mark):
        return True
    elif (tablero[3] == tablero[6] and tablero[3] == tablero[9] and tablero[3] == mark):
        return True
    elif (tablero[1] == tablero[5] and tablero[1] == tablero[9] and tablero[1] == mark):
        return True
    elif (tablero[7] == tablero[5] and tablero[7] == tablero[3] and tablero[7] == mark):
        return True
    else:
        return False


def empate():
    for lugar in tablero.keys():
        if (tablero[lugar] == ' '):
            return False
    return True

tablero = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}