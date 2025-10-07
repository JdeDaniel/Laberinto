from perceptron import *
from datos import *
from graficas import *
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap



#aprendizaje = 0.0
#epocas = 0

# Opción 1: Comparar tasas de aprendizaje
def comparar_tasas_aprendizaje():
    tasas = [0.01, 0.1, 1.0]
    colores = ['red', 'green', 'blue']
    preceptron1 = preceptron()
    datos1 = datos()
    x, y = datos1.transformar()

    for lr, color in zip(tasas, colores):
        modelo = preceptron1.entrenar(entradas=x, salidas=y, tasa_aprendizaje=lr, epocas=25)
        plt.figure(figsize=(10,5))  # <-- limpia y crea una nueva figura

        plt.subplot(1, 2, 1)
        plot_decision_regions(x, y, classifier=preceptron1)
        plt.title(f'Frontera de decisión (lr={lr})')
        plt.xlabel('Longitud del sépalo (estandarizada)')
        plt.ylabel('Ancho del sépalo (estandarizada)')
        #plt.show()

        plt.subplot(1, 2, 2)
        plt.plot(range(1, len(modelo) + 1),
                    modelo, marker='o', color=color, label=f'lr={lr}')
        plt.tight_layout()
        plt.show()

    plt.xlabel('Épocas')
    plt.ylabel('Errores')
    plt.title('Comparación de tasas de aprendizaje')
    plt.legend()
    plt.show()

# Opción 2: Comparar número de épocas
def comparar_epocas():
    epocas_lista = [10, 25, 50, 100]
    colores = ['red', 'orange', 'green', 'blue']
    preceptron1 = preceptron()
    datos1 = datos()
    x, y = datos1.transformar()

    for epocas, color in zip(epocas_lista, colores):
        modelo = preceptron1.entrenar(entradas=x, salidas=y, tasa_aprendizaje=0.1, epocas=epocas)
        plt.figure(figsize=(10,5))  # <-- limpia y crea una nueva figura

        plt.subplot(1, 2, 1)
        plot_decision_regions(x, y, classifier=preceptron1)
        plt.title(f'Frontera de decisión ({epocas} épocas)')
        plt.xlabel('Longitud del sépalo (estandarizada)')
        plt.ylabel('Ancho del sépalo (estandarizada)')

        plt.subplot(1, 2, 2)
        plt.plot(range(1, len(modelo) + 1), 
                    modelo, marker='o', color=color, label=f'Epocas = {epocas}')
        plt.tight_layout()
        plt.show()

    plt.xlabel('Épocas')
    plt.ylabel('Errores')
    plt.title('Comparación de número de épocas')
    plt.legend()
    plt.show()

# Función para ejecutar entrenamiento base
def entrenamiento_base():
    preceptron1 = preceptron()
    datos1 = datos()
    x, y = datos1.transformar()
    modelo = preceptron1.entrenar(entradas=x, salidas=y, tasa_aprendizaje=0.1, epocas=25)
    plt.figure(figsize=(10,5))  # <-- limpia y crea una nueva figura
    
    plt.subplot(1, 2, 1)
    plot_decision_regions(x, y, classifier=preceptron1)
    plt.xlabel('Longitud del sépalo (estandarizada)')
    plt.ylabel('Ancho del sépalo (estandarizada)')
    plt.title('Frontera de decisión (lr=0.1, 25 épocas)')
    plt.legend()

    plt.subplot(1, 2, 2)
    plt.plot(range(1, len(modelo) + 1),
             modelo, marker='o')
    plt.xlabel('Épocas')
    plt.ylabel('Errores')
    plt.title('Errores por época (lr=0.1)')
    plt.tight_layout()
    plt.show()

def menu():
    while True:
        print("\n=== MENÚ PRINCIPAL ===")
        print("1. Entrenamiento base (lr=0.1, 25 épocas)")
        print("2. Comparar tasas de aprendizaje (0.01, 0.1, 1.0)")
        print("3. Comparar número de épocas (10, 25, 50, 100)")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            entrenamiento_base()
        elif opcion == "2":
            comparar_tasas_aprendizaje()
        elif opcion == "3":
            comparar_epocas()
        elif opcion == "4":
            print("Saliendo del programa...")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

if __name__ == "__main__":
    menu()

    """
    def menu(): # Menu para ingresar la tasa de aprendizaje y el numero de epocas
        print("Ingrese la tasa de aprendizaje (entre 0 y 1): ")
        main.aprendizaje = float(input())
        if main.aprendizaje < 0 or main.aprendizaje > 1:
            print("La tasa de aprendizaje debe estar entre 0 y 1")
            exit()
        print("Ingrese el numero de epocas: ") 
        main.epocas = int(input())

    def main():
        while True:
            main.menu()
            datos1 = datos()
            entradas, salidas = datos1.transformar()
            perceptron = preceptron()
            perceptron.entrenar(entradas, salidas, main.aprendizaje, main.epocas)
            print("Desea continuar? (s/n)")
            opcion = input()
            if opcion.lower() != 's':
                break
    """

