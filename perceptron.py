import numpy as np

class Perceptron:
    def __init__(self, lr=0.01, n_iter=10):
        self.lr = lr              # tasa de aprendizaje (lr)
        self.n_iter = n_iter      # número de épocas (n_iter)
        self.w = None             # pesos (w)
        self.b = None             # bias (b)
        self.errores_por_epoca = []  # lista para guardar errores por época

    def fit(self, X, y):
        # === INICIALIZAR pesos y bias en cero ===
        self.w = np.zeros(X.shape[1])
        self.b = 0 # bias inicializado en 0

        # === PARA cada época hasta n_iteraciones ===
        for epoca in range(self.n_iter):
            errores = 0  # errores = 0 se reinicia al inicio para contar errores en esa época

            # === PARA cada ejemplo (xi, yi) ===
            for xi, yi in zip(X, y):

                # calcular salida = f(w . xi + b) con producto punto
                z = np.dot(xi, self.w) + self.b
                salida = self.funcion_escalon(z)

                # calcular error = yi - salida
                error = yi - salida

                # actualizar pesos: w = w + lr * error * xi
                self.w = self.w + self.lr * error * xi

                # actualizar bias: b = b + lr * error
                self.b = self.b + self.lr * error

                # si error != 0: errores += 1
                if error != 0:
                    errores += 1

            # guardar errores de la época
            self.errores_por_epoca.append(errores)

        return self

    def net_input(self, X):
        """Calcula la entrada neta w·x + b"""
        return np.dot(X, self.w) + self.b

    def funcion_escalon(self, z):
        """f(z) = 1 si z >= 0, de lo contrario 0"""
        return np.where(z >= 0.0, 1, 0)

    def predecir(self, X):
        """Predice la clase de entrada X"""
        return self.funcion_escalon(self.net_input(X))
