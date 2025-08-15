
from matriz import *
from BFS import *
from DFS import *

mapa = []
matriz = []
coordenadas = [] # creo que las coordenadas no son necesarias 
arbol = {}
Inicio = {} 

def escojer_mapa():
    archivo_txt = input("Ingresa el nombre del archivo de mapa (con .txt): ")
    mapa = cargar_mapa(archivo_txt)

    #Quitar esto en un momento
    print("Mapa:")
    for fila in mapa:
        print(fila)

    matriz = convertirmapa(mapa)
    #Quitar esto en un momento
    print("Matriz:")
    for fila in matriz:
        print(fila)

    #Quitar esto en un momento
    coordenadas = generarMatrizCoordenadas(matriz)

    #Quitar esto en un momento
    print("\nMatriz de coordenadas (-1, 1, 2):")
    for fila in coordenadas:
        print(fila) # Una vez comprobado borrar

    inicio = encontrar_inicio(matriz) 
    if inicio: # Si se encuentra el nodo de inicio
        arbol = construir_arbol(matriz, inicio) # Construye el árbol de búsqueda

        #Quitar esto en un momento
        print("\nÁrbol generado (coordenadas):") 
        for nodo, hijos in arbol.items(): # Imprime el árbol con nodos y sus hijos, borrar para entrega
            print(f"{nodo}: {hijos}")
    else:
        print("No se encontró el nodo de inicio (-1) en la matriz.") # Mensaje de error si no se encuentra el nodo de inicio


def menu():
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
                return
        elif choice == '2':
            print("You selected Option 2.")
        elif choice == '3':
            matrizLaberinto = escojer_mapa()
        elif choice == '4':
            print("Adios!")
        else:
            print("Opcion no valida.")


if __name__ == "__main__":
    menu()