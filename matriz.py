from collections import deque
from colorama import Fore, Style, init
init(autoreset=True)

def cargar_mapa(ruta_archivo):
    
    matriz = []

    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            matriz.append(linea.strip())
    return matriz

def convertirmapa(matriz):
    # Diccionario de conversión de caracteres a valores numéricos
    conversion = {
        '#': 0,
        '.': 1,
        'S': -1,
        'G': 2
    }

    newMatriz = []

    for linea in matriz:
        # Elimina saltos de línea 
        fila = [conversion.get(caracter, None) for caracter in linea.strip()]
        newMatriz.append(fila)

    return newMatriz

def encontrar_inicio(matriz): # Encuentra la posición del nodo de inicio (-1)
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == -1:
                return (i, j)
    return None

def construir_arbol(matriz, inicio):
    arbol = {}
    visitados = set()
    queue = deque([inicio])
    visitados.add(inicio)

    # Movimientos: arriba, abajo, izquierda, derecha
    movimientos = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue:
        actual = queue.popleft()
        hijos = []
        for dx, dy in movimientos:
            nx, ny = actual[0] + dx, actual[1] + dy
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]):
                if matriz[nx][ny] == 1 or matriz[nx][ny] == 2:  # Solo agrega nodos con valor 1 o 2
                    hijos.append((nx, ny))  # Agrega todos los hijos con valor 1, aunque ya hayan sido visitados
                    if (nx, ny) not in visitados:
                        queue.append((nx, ny))
                        visitados.add((nx, ny))
        arbol[actual] = hijos
    return arbol

def bfs_camino(matriz, arbol, inicio):

    # Buscar la posición del objetivo (2)
    objetivo = None
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == 2:
                objetivo = (i, j)
                break
        if objetivo:
            print("Objetivo encontrado en:", objetivo)
            break

    if not objetivo:
        print("No se encontró el nodo objetivo (2) en la matriz.")
        return None

    # BFS para encontrar el camino
    queue = deque()
    queue.append((inicio, [inicio]))  # (nodo_actual, camino_hasta_ahora)
    visitados = set()
    visitados.add(inicio)

    while queue:
        actual, camino = queue.popleft()
        if actual == objetivo:
            return camino
        for hijo in arbol.get(actual, []):
            if hijo not in visitados:
                queue.append((hijo, camino + [hijo]))
                visitados.add(hijo)
    print("No hay camino del inicio al objetivo.")
    return None

def dfs_camino(matriz, arbol, inicio):
    # Buscar la posición del objetivo (2)
    objetivo = None
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == 2:
                objetivo = (i, j)
                break
        if objetivo:
            break

    if not objetivo:
        print("No se encontró el nodo objetivo (2) en la matriz.")
        return None

    stack = [(inicio, [inicio])]
    visitados = set()
    visitados.add(inicio)

    while stack:
        actual, camino = stack.pop()
        if actual == objetivo:
            return camino
        for hijo in arbol.get(actual, []):
            if hijo not in visitados:
                stack.append((hijo, camino + [hijo]))
                visitados.add(hijo)
    print("No hay camino del inicio al objetivo (DFS).")
    return None


def mostrar_laberinto_coloreado(matriz, camino, titulo):
    print(f"\n{titulo}")
    for i, fila in enumerate(matriz):
        linea = ""
        for j, valor in enumerate(fila):
            if (i, j) in camino:
                linea += Fore.GREEN + "●" + Style.RESET_ALL  # Camino en verde
            elif valor == 0:
                linea += Fore.YELLOW + "#" + Style.RESET_ALL  # Pared en amarillo
            elif valor == 1:
                linea += Fore.YELLOW + "." + Style.RESET_ALL  # Camino libre en amarillo
            elif valor == -1:
                linea += Fore.YELLOW + "S" + Style.RESET_ALL  # Inicio en amarillo
            elif valor == 2:
                linea += Fore.YELLOW + "G" + Style.RESET_ALL  # Meta en amarillo
            else:
                linea += " "
        print(linea)
