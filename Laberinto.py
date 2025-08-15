from collections import deque
from colorama import Fore, Style, init
init(autoreset=True)

def bfs_camino(matriz, arbol, inicio):
    print(inicio)

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