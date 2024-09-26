def mostrar_cabecera():
    # Imprimir la cabecera con nombre y universidad
    print("=" * 50)
    print("Bienvenidos a mi programa, soy Patricia Matute Zambrano!")
    print("Estudiante de la Universidad Estatal Amazónica")
    print("=" * 50)
mostrar_cabecera()
print("Este es un ejemplo de cómo puedes Trabajar con Diccionarios en Python.")
# Empezamos
# Aquí creo el Diccionario llamado Información Personal
informacion_personal = {
    "nombre": "Juan Pérez",  # Nombre de la persona
    "edad": 32,  # Edad de la persona
    "ciudad": "Quito",  # Ciudad inicial
    "profesion": "Ingeniero"  # Profesión inicial
}

# Se Accede al valor asociado con la clave "ciudad" y se lo modifica
informacion_personal["ciudad"] = "Guayaquil"  # Cambia la ciudad a "Guayaquil"

# Aquí  agrego  una nueva clave-valor al diccionario para representar la "profesion"
informacion_personal["profesion"] = "Desarrollador de Software"  # Nueva profesión

# Se verifica si la clave "telefono" existe en el diccionario
# Si no existe, se agrega con un número ficticio
if "telefono" not in informacion_personal:
    informacion_personal["telefono"] = "0987654321"  # Número ficticio

# Se elimina la clave "edad" del diccionario, ya que no es necesaria
del informacion_personal["edad"]

# Se imprime el diccionario resultante después de realizar todas las operaciones
print(informacion_personal)
