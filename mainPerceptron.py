from perceptron import Perceptron
from graficas import plot_decision_regions
from sklearn.datasets import load_iris
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# ------------------------------------------------------------
# 1. Cargar y preparar el dataset Iris
# ------------------------------------------------------------
iris = load_iris()
X = iris.data[:100, :2]   # Dos primeras clases y características, los primero 100 ejemplos
y = iris.target[:100] # Las primeras 100 etiquetas
y = (y == 1).astype(int)  # Clases Setosa=0, Versicolor=1 -> Binario 0 y 1

# Normalización (z-score)
sc = StandardScaler()
X_std = sc.fit_transform(X)


# Función para ejecutar entrenamiento base
def entrenamiento_base():
    modelo = Perceptron(lr=0.1, n_iter=25)
    modelo.fit(X_std, y)

    plt.plot(range(1, len(modelo.errores_por_epoca) + 1),
             modelo.errores_por_epoca, marker='o')
    plt.xlabel('Épocas')
    plt.ylabel('Errores')
    plt.title('Errores por época (lr=0.1)')
    plt.show()

    plt.figure()
    
    plot_decision_regions(X_std, y, classifier=modelo)
    plt.xlabel('Longitud del sépalo (estandarizada)')
    plt.ylabel('Ancho del sépalo (estandarizada)')
    plt.title('Frontera de decisión (lr=0.1, 25 épocas)')
    plt.legend()
    plt.show()

# Opción 1: Comparar tasas de aprendizaje
def comparar_tasas_aprendizaje():
    tasas = [0.01, 0.1, 1.0]
    colores = ['red', 'green', 'blue']

    for lr, color in zip(tasas, colores):
        modelo = Perceptron(lr=lr, n_iter=25)
        modelo.fit(X_std, y)
        plt.figure()  # <-- limpia y crea una nueva figura

        plot_decision_regions(X_std, y, classifier=modelo)
        plt.title(f'Frontera de decisión (lr={lr})')
        plt.xlabel('Longitud del sépalo (estandarizada)')
        plt.ylabel('Ancho del sépalo (estandarizada)')
        plt.show()

        plt.plot(range(1, len(modelo.errores_por_epoca) + 1),
                 modelo.errores_por_epoca, marker='o', color=color, label=f'lr={lr}')

    plt.xlabel('Épocas')
    plt.ylabel('Errores')
    plt.title('Comparación de tasas de aprendizaje')
    plt.legend()
    plt.show()


# Opción 2: Comparar número de épocas

def comparar_epocas():
    epocas_lista = [10, 25, 50, 100]
    colores = ['red', 'orange', 'green', 'blue']

    for epocas, color in zip(epocas_lista, colores):
        modelo = Perceptron(lr=0.1, n_iter=epocas)
        modelo.fit(X_std, y)
        plt.figure()  # <-- limpia y crea una nueva figura

        plot_decision_regions(X_std, y, classifier=modelo)
        plt.title(f'Frontera de decisión ({epocas} épocas)')
        plt.xlabel('Longitud del sépalo (estandarizada)')
        plt.ylabel('Ancho del sépalo (estandarizada)')
        plt.show()

        plt.plot(range(1, len(modelo.errores_por_epoca) + 1),
                 modelo.errores_por_epoca, marker='o', color=color, label=f'{epocas} épocas')

    plt.xlabel('Épocas')
    plt.ylabel('Errores')
    plt.title('Comparación de número de épocas')
    plt.legend()
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
