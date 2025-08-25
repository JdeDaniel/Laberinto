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
    queue = deque()
    queue.append((inicio, [inicio], 0))  # (nodo_actual, camino_hasta_ahora, costo_acumulado)
    visitados = set()
    visitados.add(inicio)
    mejor_camino = None
    
    while queue:
        print("Cola actual:", queue) # Imprime el estado actual de la cola
        actual, camino, costo = queue.popleft()
        if actual == objetivo: 
            if mejor_camino is None or costo < mejor_camino[1]:
                mejor_camino = (camino, costo)

        for dx, dy in [(-1,0), (1,0), (0,-1), (0,1)]: # Pasos posibles: arriba, abajo, izquierda, derecha
            nx, ny = actual[0] + dx, actual[1] + dy
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]) and matriz[nx][ny] != 0:
                if matriz[nx][ny] != 0 and (nx, ny) not in visitados:
                    nuevo_costo = costo + matriz[nx][ny]
                    queue.append(((nx, ny), camino + [(nx, ny)], nuevo_costo))
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