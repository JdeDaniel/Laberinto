from sklearn.datasets import load_iris
from numpy import *
from sklearn.preprocessing import MinMaxScaler

class datos:
    iris = load_iris()

    def __init__(self):
        pass

    def transformar(self):
        datos_transformados = self.iris.data[:100, :2] #Tomamos solo las dos primeras características y los primeros 100 datos
        target = self.iris.target[:100] #Tomamos solo los 100 primeros targets
        scaler = MinMaxScaler()
        datos_transformados = scaler.fit_transform(datos_transformados) #Normalizamos los datos entre 0 y 1
        return datos_transformados, target
