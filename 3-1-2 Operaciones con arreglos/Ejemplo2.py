# Definimos la función para realizar el algoritmo de Bubble Sort
def bubble_sort(fila):
    n = len(fila)  # Longitud de la fila
    for i in range(n):
        for j in range(0, n-i-1):
            # Intercambiamos los elementos si el actual es mayor que el siguiente
            if fila[j] > fila[j+1]:
                fila[j], fila[j+1] = fila[j+1], fila[j]

# Definimos la función para ordenar una fila específica de la matriz
def ordenar_fila_matriz(matriz, fila_a_ordenar):
    # Mostramos la matriz original
    print("Matriz original:")
    for fila in matriz:
        print(fila)

    # Ordenamos la fila específica usando Bubble Sort
    bubble_sort(matriz[fila_a_ordenar])

    # Mostramos la matriz con la fila ordenada
    print(f"\nMatriz después de ordenar la fila {fila_a_ordenar}:")
    for fila in matriz:
        print(fila)

# Creamos la matriz bidimensional de 3x3 con valores numéricos
matriz = [
    [9, 3, 7],
    [5, 1, 8],
    [4, 6, 2]
]

# Especificamos cuál fila queremos ordenar (por ejemplo, la segunda fila: índice 1)
fila_a_ordenar = 1

# Llamamos a la función para ordenar la fila
ordenar_fila_matriz(matriz, fila_a_ordenar)
