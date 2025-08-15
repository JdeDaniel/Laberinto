from collections import deque
from colorama import Fore, Style, init
init(autoreset=True)

def cargar_mapa(ruta_archivo):
    # Diccionario de conversión de caracteres a valores numéricos
    conversion = {
        '#': 0,
        '.': 1,
        'S': -1,
        'G': 2
    }

    matriz = []

    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Elimina saltos de línea 
            fila = [conversion.get(caracter, None) for caracter in linea.strip()]
            matriz.append(fila)

    return matriz

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




if __name__ == "__main__":
    archivo_txt = input("Ingresa el nombre del archivo de mapa (con .txt): ")
    matriz_resultado = cargar_mapa(archivo_txt)

    print("Matriz generada:")
    for fila in matriz_resultado:
        print(fila)
    
        # Generar matriz de coordenadas para -1, 1 o 2
    matriz_coordenadas = []
    for i, fila in enumerate(matriz_resultado):
        fila_coord = []
        for j, valor in enumerate(fila):
            if valor in (-1, 1, 2):
                fila_coord.append((i, j))
            else:
                fila_coord.append(0)
        matriz_coordenadas.append(fila_coord)

    print("\nMatriz de coordenadas (-1, 1, 2):")
    for fila in matriz_coordenadas:
        print(fila) # Una vez comprobado borrar
    
    inicio = encontrar_inicio(matriz_resultado) 
    if inicio: # Si se encuentra el nodo de inicio
        arbol = construir_arbol(matriz_resultado, inicio) # Construye el árbol de búsqueda
        print("\nÁrbol generado (coordenadas):") 
        for nodo, hijos in arbol.items(): # Imprime el árbol con nodos y sus hijos, borrar para entrega
            print(f"{nodo}: {hijos}")
    else:
        print("No se encontró el nodo de inicio (-1) en la matriz.") # Mensaje de error si no se encuentra el nodo de inicio

        # Buscar y mostrar el camino del inicio al objetivo
    camino = bfs_camino(matriz_resultado, arbol, inicio)
    if camino:
        mostrar_laberinto_coloreado(matriz_resultado, camino, "Laberinto con camino BFS (verde)")
        print(f"Pasos necesarios del origen a la meta: {len(camino) - 1}")
    else:
        print("No se encontró un camino del inicio al objetivo.")
    
        # Buscar y mostrar el camino usando DFS
    camino_dfs = dfs_camino(matriz_resultado, arbol, inicio)
    if camino_dfs:
        mostrar_laberinto_coloreado(matriz_resultado, camino_dfs, "Laberinto con camino DFS (verde)")
        print(f"Pasos necesarios del origen a la meta (DFS): {len(camino_dfs) - 1}")
    else:
        print("No se encontró un camino del inicio al objetivo (DFS).")


    
