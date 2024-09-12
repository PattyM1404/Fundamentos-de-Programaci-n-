def calcular_temperatura_promedio(ciudades_temperaturas):
    """
    Función para calcular la temperatura promedio de múltiples ciudades durante 4 semanas.

    """
    # Diccionari  para almacenar las temperaturas promedio de cada ciudad
    promedios_ciudades = {}

    # Iterar sobre cada ciudad
    for ciudad, temperaturas in ciudades_temperaturas.items():
        # Calcular la temperatura promedio para la ciudad
        promedio = sum(temperaturas) / len(temperaturas)

        # Guardar el resultado en el diccionario de promedios
        promedios_ciudades[ciudad] = promedio

    # Retornar el diccionario con los promedios
    return promedios_ciudades


# Ejemplo de datos: 3 ciudades con temperaturas registradas durante 4 semanas
datos_ciudades = {
    "Quito": [18, 20, 19, 21],
    "Guayaquil": [30, 31, 32, 33],
    "Cuenca": [15, 16, 14, 17]
}

# Llamar a la función y calcular el promedio de cada ciudad
promedios = calcular_temperatura_promedio(datos_ciudades)

# Mostrar el resultado
for ciudad, promedio in promedios.items():
    print(f"La temperatura promedio de {ciudad} es {promedio:.2f}°C")
