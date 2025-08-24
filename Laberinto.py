from collections import deque
from colorama import Fore, Style, init
import time
init(autoreset=True)

def bfs_camino(matriz, arbol, inicio):
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

    # BFS para encontrar el camino
    star = time.time()
    queue = deque()
    queue.append((inicio, [inicio]))  # (nodo_actual, camino_hasta_ahora)
    visitados = set()
    visitados.add(inicio)

    while queue:
        actual, camino = queue.popleft()
        if actual == objetivo:
            end = time.time()
            print(f"==BFS==")
            print(f"Longitud de la ruta: {len(camino) - 1}")
            print(f"Nodos visitados: {len(visitados) - 1}")
            print(f"Tiempo de ejecución: {end - star} segundos")
            mostrar_laberinto_coloreado(matriz, camino, "Laberinto con camino BFS (verde)")

        for hijo in arbol.get(actual, []):
            if hijo not in visitados:
                queue.append((hijo, camino + [hijo]))
                visitados.add(hijo)

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

    star = time.time()
    stack = [(inicio, [inicio])]
    visitados = set()
    visitados.add(inicio)

    while stack:
        actual, camino = stack.pop()
        if actual == objetivo:
            end = time.time()
            print(f"==DFS==")
            print(f"Longitud de la ruta: {len(camino) - 1}")
            print(f"Nodos visitados: {len(visitados) - 1}")
            print(f"Tiempo de ejecución: {end - star} segundos")
            mostrar_laberinto_coloreado(matriz, camino, "Laberinto con camino DFS (verde)")
        for hijo in arbol.get(actual, []):
            if hijo not in visitados:
                stack.append((hijo, camino + [hijo]))
                visitados.add(hijo)

def costos_camino(matriz, arbol, inicio):
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

    # BFS para encontrar el camino
    star = time.time()
    queue = deque()
    queue.append((inicio, [inicio], 0))  # (nodo_actual, camino_hasta_ahora, costo_acumulado)
    visitados = set()
    visitados.add(inicio)

    while queue:
        actual, camino, costo = queue.popleft()
        if actual == objetivo:
            end = time.time()
            print(f"==Costos==")
            print(f"Longitud de la ruta: {len(camino) - 1}")
            print(f"Costo total del camino: {costo - 2}")
            print(f"Nodos visitados: {len(visitados) - 1}")
            print(f"Tiempo de ejecución: {end - star} segundos")
            mostrar_laberinto_coloreado(matriz, camino, "Laberinto con camino Costos (verde)")

        for hijo in arbol.get(actual, []):
            if hijo not in visitados:
                print(matriz[hijo[0]][hijo[1]])
                nuevo_costo = costo + matriz[hijo[0]][hijo[1]]  # Asumiendo un costo uniforme de 1 por movimiento
                queue.append((hijo, camino + [hijo], nuevo_costo))
                visitados.add(hijo)

def mostrar_laberinto_coloreado(matriz, camino, titulo):
    print(f"\n{titulo}")
    for i, fila in enumerate(matriz):
        linea = ""
        for j, valor in enumerate(fila):
            if valor == -1:
                linea += Fore.YELLOW + "S" + Style.RESET_ALL  # Inicio en amarillo
            elif valor == 2:
                linea += Fore.RED + "G" + Style.RESET_ALL  # Meta en amarillo
            elif (i, j) in camino:
                linea += Fore.GREEN + "●" + Style.RESET_ALL  # Camino en verde
            elif valor == 0:
                linea += Fore.WHITE + "#" + Style.RESET_ALL  # Pared en amarillo
            elif valor == 1:
                linea += Fore.WHITE + "." + Style.RESET_ALL  # Camino libre en amarillos
            else:
                linea += " "
        print(linea)
    return None