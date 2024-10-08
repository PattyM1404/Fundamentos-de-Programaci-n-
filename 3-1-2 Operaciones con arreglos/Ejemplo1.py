# Definimos una función para buscar un valor dentro de la matriz bidimensional
def buscar_en_matriz(matriz, valor_a_buscar):
    # Recorremos la matriz usando dos bucles anidados (filas y columnas)
    for i in range(len(matriz)):  # Bucle para recorrer las filas
        for j in range(len(matriz[i])):  # Bucle para recorrer las columnas
            # Verificamos si el valor actual es igual al valor que buscamos
            if matriz[i][j] == valor_a_buscar:
                # Si encontramos el valor, mostramos un mensaje con su posición
                print(f"Valor {valor_a_buscar} encontrado en la posición ({i}, {j})")
                return  # Terminamos la búsqueda porque ya encontramos el valor
    # Si terminamos de recorrer toda la matriz y no encontramos el valor, mostramos un mensaje
    print(f"Valor {valor_a_buscar} no encontrado en la matriz")

# Creamos una matriz bidimensional de 3x3 con valores numéricos
matriz = [
    [4, 9, 2],
    [3, 5, 7],
    [8, 1, 6]
]
print(matriz)
# Definimos el valor que queremos buscar en la matriz
valor = 7

# Llamamos a la función para buscar el valor en la matriz
buscar_en_matriz(matriz, valor)
