
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