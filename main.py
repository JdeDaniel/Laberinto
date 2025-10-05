from perceptron import *
from datos import *

class main:

    aprendizaje = 0.0
    epocas = 0

    def menu():
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
        

main.main()