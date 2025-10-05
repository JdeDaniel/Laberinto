class preceptron:
    
    peso1, peso2, bias = 0.0, 0.0, 0.0

    def entrenar(self, entradas, salidas, tasa_aprendizaje, epocas):
        errores = [] # Lista para almacenar el número de errores en cada época
        for _ in range(epocas):
            error_epoca = 0 # Contador de errores en la época actual
            for i in range(len(entradas)):
                suma_ponderada = (entradas[i][0] * self.peso1) + (entradas[i][1] * self.peso2) + self.bias #Cálculo de la suma ponderada
                salida_predicha = 1 if suma_ponderada >= 0 else 0 #Función de activación escalón
                error = salidas[i] - salida_predicha #Cálculo del error
                # Actualización de pesos y bias
                self.peso1 += tasa_aprendizaje * error * entradas[i][0]
                self.peso2 += tasa_aprendizaje * error * entradas[i][1]
                self.bias += tasa_aprendizaje * error
                if error != 0: # Si hubo un error, incrementamos el contador
                    error_epoca += 1
            errores.append(error_epoca) # Almacenamos el número de errores de la época actual