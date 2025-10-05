from sklearn.datasets import load_iris
from numpy import *
from sklearn.preprocessing import MinMaxScaler

class datos:
    iris = load_iris()

    def __init__(self):
        pass

    def transformar(self):
        datos_transformados = self.iris.data[:100, :2]
        target = self.iris.target[:100]
        scaler = MinMaxScaler()
        datos_transformados = scaler.fit_transform(datos_transformados)
        print(datos_transformados)
        print(target)
        return datos_transformados, target


    def imprimir(self):
        print(self.iris.target_names)
        print(self.iris.target)
