def cargar_mapa(ruta_archivo):
    # Diccionario de conversión de caracteres a valores numéricos
    conversion = {
        '#': 0,
        '.': 1,
        'S': -1,
        'G': 2
    }

    matriz = []

    with open(ruta_archivo, 'r') as archivo:
        for linea in archivo:
            # Elimina saltos de línea y crea una fila convertida
            fila = [conversion.get(caracter, None) for caracter in linea.strip()]
            matriz.append(fila)

    return matriz


# Ejemplo de uso
if __name__ == "__main__":
    archivo_txt = input("Ingresa el nombre del archivo de mapa (con .txt): ")
    matriz_resultado = cargar_mapa(archivo_txt)

    print("Matriz generada:")
    for fila in matriz_resultado:
        print(fila)
