
from matriz import *
from Laberinto import *

mapa = []
matriz = []
coordenadas = [] # creo que las coordenadas no son necesarias 
arbol = {}
Inicio = ()

def escojer_mapa():
    global mapa, matriz, coordenadas, arbol, Inicio
    archivo_txt = input("Ingresa el nombre del archivo de mapa (con .txt): ")
    mapa = cargar_mapa(archivo_txt)

    #Quitar esto en un momento
    """
    print("Mapa:")
    for fila in mapa:
        print(fila)
    """
    matriz = convertirmapa(mapa)

    """
    #Quitar esto en un momento
    print("Matriz:")
    for fila in matriz:
        print(fila)
    """

    coordenadas = generarMatrizCoordenadas(matriz)

    """
    #Quitar esto en un momento
    print("\nMatriz de coordenadas (-1, 1, 2):")
    for fila in coordenadas:
        print(fila) # Una vez comprobado borrar
    """

    Inicio = encontrar_inicio(matriz) 
    if Inicio: # Si se encuentra el nodo de inicio
        arbol = construir_arbol(matriz, Inicio) # Construye el árbol de búsqueda

        """
        #Quitar esto en un momento
        print("\nÁrbol generado (coordenadas):") 
        for nodo, hijos in arbol.items(): # Imprime el árbol con nodos y sus hijos, borrar para entrega
            print(f"{nodo}: {hijos}")
    else:
        print("No se encontró el nodo de inicio (-1) en la matriz.") # Mensaje de erro  r si no se encuentra el nodo de inicio
        """


def menu():
    global mapa, matriz, coordenadas, arbol, Inicio
    choice = 0
    while choice != '4':
        print("Menu")
        print("1. Resolver por BFS")
        print("2. Resolver por DFS")
        print("3. Cambiar laberinto")
        print("4. Salir")
        choice = input("Por favor selecciona una opcion (1-4): ")
        

        if choice == '1':
            if arbol == None:
                print("No se ha escojido ningún laberinto. Por favor, elige un laberinto primero.")
            else:
                bfs_camino(matriz, arbol, Inicio)
        elif choice == '2':
            if arbol == None:
                print("No se ha escojido ningún laberinto. Por favor, elige un laberinto primero.")
            else:
                dfs_camino(matriz, arbol, Inicio)
        elif choice == '3':
            matrizLaberinto = escojer_mapa()
        elif choice == '4':
            print("Adios!")
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()