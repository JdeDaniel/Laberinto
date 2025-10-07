import numpy as np

class preceptron:

    def __init__(self):
        self.pesos = None
        self.bias = 0.0
        self.errores_por_epoca = []

    def entrenar(self, entradas, salidas, tasa_aprendizaje, epocas):
        # Reiniciamos pesos y bias antes de entrenar
        self.bias = 0.0 
        self.pesos = np.zeros(entradas.shape[1])
        errores = [] # Lista para almacenar el número de errores en cada época
        for _ in range(epocas):
            error_epoca = 0 # Contador de errores en la época actual
            for xi, yi in zip(entradas, salidas):
                suma_ponderada = np.dot(xi, self.pesos)+ self.bias #Cálculo de la suma ponderada
                salida_predicha = 1 if suma_ponderada >= 0 else 0 #Función de activación escalón
                error = yi - salida_predicha #Cálculo del error
                # Actualización de pesos y bias
                self.pesos += tasa_aprendizaje * error * xi
                self.bias += tasa_aprendizaje * error
                if error != 0: # Si hubo un error, incrementamos el contador
                    error_epoca += 1
            errores.append(error_epoca) # Almacenamos el número de errores de la época actual
        return errores
    
    def predecir(self, entradas):
        entradas = np.array(entradas)
        salida = np.dot(entradas, self.pesos)+ self.bias
        return (salida >= 0).astype(int)