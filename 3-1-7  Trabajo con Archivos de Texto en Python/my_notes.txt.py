def mostrar_cabecera():
    # Imprimir la cabecera con nombre y universidad
    print("=" * 50)
    print("Bienvenidos a mi programa, soy Patricia Matute Zambrano!")
    print("Estudiante de la Universidad Estatal Amazónica")
    print("=" * 50)
mostrar_cabecera()
print("Este es un ejemplo de cómo puedes Trabajar con Archivos de Texto en Python.")
# Empezamos
# Escritura de archivo de texto
# Creamos un nuevo archivo llamado my_notes.txt y escribimos notas personales

# Abrir (o crear) el archivo en modo escritura
with open('my_notes.txt', 'w') as file:
    # Escribimos notas personales en el archivo usado el metodo write
    file.write("Nota 1: Estudiar para el examen de matemáticas.\n")
    file.write("Nota 2: Comprar víveres para la semana.\n")
    file.write("Nota 3: Llamar a mamá el fin de semana.\n")

# Lectura de archivo de texto
# Abrimos el archivo en modo lectura
with open('my_notes.txt', 'r') as file:
    # Leer línea por línea y mostrar en consola
    for line in file:
        print(line.strip())  # Usar strip() para quitar el salto de línea al final
# El archivo se cierra automáticamente al usar "with" en ambas operaciones