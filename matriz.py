from collections import deque

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
        'G': 2,
        ',': 5,  # Coma como un tipo de terreno dificil 
        '~': 10  # Agua
    }

    newMatriz = []

    for linea in matriz:
        # Elimina saltos de línea 
        fila = [conversion.get(caracter, None) for caracter in linea.strip() if caracter != ' ']
        newMatriz.append(fila)

    return newMatriz

def encontrar_inicio(matriz): # Encuentra la posición del nodo de inicio (-1)
    for i, fila in enumerate(matriz):
        for j, valor in enumerate(fila):
            if valor == -1:
                return (i, j)
    return None

def construir_arbol(matriz, inicio): # Construye un árbol de búsqueda a partir del nodo de inicio
    arbol = {}
    visitados = set()
    queue = deque([inicio])
    visitados.add(inicio)

    # Movimientos: arriba, abajo, izquierda, derecha
    movimientos = [(-1,0), (1,0), (0,-1), (0,1)]

    while queue: # Mientras haya nodos en la cola
        actual = queue.popleft() # Extrae el nodo actual de la cola
        hijos = [] # Lista de hijos del nodo actual
        for dx, dy in movimientos: 
            nx, ny = actual[0] + dx, actual[1] + dy # Calcula las nuevas coordenadas
            if 0 <= nx < len(matriz) and 0 <= ny < len(matriz[0]): # Verifica que las coordenadas estén dentro de los límites de la matriz
                if (matriz[nx][ny] != 0 and matriz [nx][ny] != -1)  and (nx, ny) not in visitados: # Si la celda es transitable y no ha sido visitada
                    hijos.append((nx, ny)) # Agrega la celda como hijo del nodo actual
                    queue.append((nx, ny)) 
                    visitados.add((nx, ny))
        arbol[actual] = hijos # Añade el nodo actual y sus hijos al árbol
    return arbol 

def generarMatrizCoordenadas(matriz):
    matriz_coordenadas = []
    for i, fila in enumerate(matriz):
        fila_coord = []
        for j, valor in enumerate(fila):
            if valor in (-1, 1, 2):
                fila_coord.append((i, j))
            else:
                fila_coord.append(0)
        matriz_coordenadas.append(fila_coord)
    return matriz_coordenadas



"""
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
"""