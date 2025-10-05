class preceptron:
    
    peso1, peso2, bias = 0.0, 0.0, 0.0

    def entrenar(self, entradas, salidas, tasa_aprendizaje, epocas):
        errores = []
        for _ in range(epocas):
            error_epoca = 0
            for i in range(len(entradas)):
                suma_ponderada = (entradas[i][0] * self.peso1) + (entradas[i][1] * self.peso2) + self.bias
                salida_predicha = 1 if suma_ponderada >= 0 else 0
                error = salidas[i] - salida_predicha
                self.peso1 += tasa_aprendizaje * error * entradas[i][0]
                self.peso2 += tasa_aprendizaje * error * entradas[i][1]
                self.bias += tasa_aprendizaje * error
                if error != 0:
                    error_epoca += 1
            errores.append(error_epoca)