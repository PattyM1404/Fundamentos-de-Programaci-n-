import random

# Aquí definino las dimensiones de la matriz 3D
ciudades = ["Ciudad1", "Ciudad2", "Ciudad3"]
dias_de_la_semana = ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
semanas = 4

# Aquí creo  la matriz 3D con temperaturas aleatorias entre 15 y 35 grados
temperaturas = [[[random.uniform(15, 35) for _ in dias_de_la_semana] for _ in range(semanas)] for _ in ciudades]

# Iterar sobre las ciudades y semanas para calcular el promedio de temperaturas por semana
for i, ciudad in enumerate(ciudades):
    print(f"\nPromedio de temperaturas para {ciudad}:")
    for semana in range(semanas):
        suma_temperaturas = 0
        for dia in range(len(dias_de_la_semana)):
            suma_temperaturas += temperaturas[i][semana][dia]
        promedio = suma_temperaturas / len(dias_de_la_semana)
        print(f"Semana {semana + 1}: {promedio:.2f} grados")
