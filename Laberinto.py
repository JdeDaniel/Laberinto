from collections import deque
from colorama import Fore, Style, init
import time
import heapq
import math
init(autoreset=True)

def calcular_costo_camino(matriz, camino):
    # Suma los valores de la matriz en las posiciones del camino, excepto el inicio
    return sum(matriz[i][j] for i, j in camino[1:])

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
            costo_total = calcular_costo_camino(matriz, camino)
            print(f"==BFS==")
            print(f"Cambio")
            print(f"Longitud de la ruta: {len(camino) - 1}")
            print(f"Costo total del camino: {costo_total}")
            print(f"Nodos visitados: {len(visitados) - 1}")
            print(f"Tiempo de ejecución: {end - star} segundos")
            mostrar_laberinto_coloreado(matriz, camino, "Laberinto con camino BFS (verde)")
            return

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
            costo_total = calcular_costo_camino(matriz, camino)
            print(f"==DFS==")
            print(f"Longitud de la ruta: {len(camino) - 1}")
            print(f"Costo total del camino: {costo_total}")
            print(f"Nodos visitados: {len(visitados) - 1}")
            print(f"Tiempo de ejecución: {end - star} segundos")
            mostrar_laberinto_coloreado(matriz, camino, "Laberinto con camino DFS (verde)")
        for hijo in arbol.get(actual, []):
            if hijo not in visitados:
                stack.append((hijo, camino + [hijo]))
                visitados.add(hijo)

def costos_camino(matriz, inicio):
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

    # Costos Uniformes para encontrar el camino
    star = time.time()
    queue = []
    heapq.heappush(queue, (0, inicio, [inicio]))  # (costo, nodo_actual, camino_hasta_ahora)
    visitados = set()
    visitados.add(inicio)
    mejor_camino = None
    
    while queue:
        costo, actual, camino= heapq.heappop(queue)
        if actual == objetivo: 
            if mejor_camino is None or costo < mejor_camino[1]:
                mejor_camino = (camino, costo)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]: # Pasos posibles: arriba, abajo, izquierda, derecha
            nx, ny = actual[0] + dx, actual[1] + dy
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]) and matriz[nx][ny] != 0:
                if matriz[nx][ny] != 0 and (nx, ny) not in visitados:
                    nuevo_costo = costo + matriz[nx][ny]
                    heapq.heappush(queue, (nuevo_costo, (nx, ny), camino + [(nx, ny)]))
                    if (matriz[nx][ny] != 2):
                        visitados.add((nx, ny))

    if mejor_camino:
        end = time.time()
        camino, costo = mejor_camino
        print(f"==Costos Uniformes==")
        print(f"Longitud de la ruta: {len(camino) - 1}")
        print(f"Costo total del camino: {costo -2}")
        print(f"Nodos visitados: {len(visitados) - 1}")
        print(f"Tiempo de ejecución: {end - star} segundos")
        mostrar_laberinto_coloreado(matriz, camino, "Laberinto con camino Costos Uniformes (verde)")

def buscar_objetivo(matriz):
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == 2:
                print("Objetivo encontrado en:", (i, j))
                return (i, j)

    return None

# ---------------- NUEVO: Algoritmo A* ---------------- #
def a_estrella_camino(matriz, inicio, heuristica="manhattan"):
    objetivo = buscar_objetivo(matriz)
    if not objetivo:
        print("No se encontró el nodo objetivo (2) en la matriz.")
        return None

    def heuristica_func(nodo):
        if heuristica == "euclidiana":
            return math.sqrt((nodo[0] - objetivo[0])**2 + (nodo[1] - objetivo[1])**2)
        else:  # Manhattan por defecto
            return abs(nodo[0] - objetivo[0]) + abs(nodo[1] - objetivo[1])

    star = time.time()
    queue = []
    heapq.heappush(queue, (heuristica_func(inicio), 0, inicio))
    visitados = set()
    padres = {inicio: None}
    g_score = {inicio: 0}
    h_score = {inicio: heuristica_func(inicio)}

    while queue:
        f, costo, actual = heapq.heappop(queue)
        if actual == objetivo:
            # Reconstruir el camino usando el diccionario de padres
            camino = []
            nodo = actual
            while nodo is not None:
                camino.append(nodo)
                nodo = padres[nodo]
            camino.reverse()
            end = time.time()
            print(f"==A* ({heuristica.capitalize()})==")
            print(f"Longitud de la ruta: {len(camino) - 1}")
            print(f"Costo total del camino: {g_score[actual]}")
            print(f"Nodos visitados: {len(visitados)}")
            print(f"Tiempo de ejecución: {end - star} segundos")
            print(f"g(n) de cada nodo: {g_score}")
            print(f"h(n) de cada nodo: {h_score}")
            mostrar_laberinto_coloreado(matriz, camino, f"Laberinto con camino A* ({heuristica}) (verde)")
            return

        if actual in visitados:
            continue
        visitados.add(actual)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]:
            nx, ny = actual[0] + dx, actual[1] + dy
            vecino = (nx, ny)
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]) and matriz[nx][ny] != 0:
                tentative_g = g_score[actual] + matriz[nx][ny]
                if vecino not in g_score or tentative_g < g_score[vecino]:
                    padres[vecino] = actual
                    g_score[vecino] = tentative_g
                    h_score[vecino] = heuristica_func(vecino)
                    f_nuevo = tentative_g + h_score[vecino]
                    heapq.heappush(queue, (f_nuevo, tentative_g, vecino))
#nuevo

def mostrar_laberinto_coloreado(matriz, camino, titulo):
    print(f"\n{titulo}")
    symbol_map = {
        -1: "S",
        2: "G",
        0: "#",
        1: ".",
        5: ",",
        10: "~"
    }
    color_map = {
        -1: Fore.YELLOW,
        2: Fore.RED,
        0: Fore.WHITE,
        1: Fore.WHITE,
        5: Fore.MAGENTA,
        10: Fore.BLUE
    }
    for i, fila in enumerate(matriz):
        linea = ""
        for j, valor in enumerate(fila):
            simbolo = symbol_map.get(valor, " ")
            if (i, j) in camino and valor not in (-1, 2):
                color = Fore.GREEN
            else:
                color = color_map.get(valor, Fore.WHITE)
            linea += color + simbolo + Style.RESET_ALL
        print(linea)
    return None