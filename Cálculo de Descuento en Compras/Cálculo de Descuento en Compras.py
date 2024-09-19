# Aquí defino la función para calcular el descuento
def calcular_descuento(monto_total, porcentaje_descuento=10):
    # Calcula el descuento aplicando el porcentaje
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Programa principal

# Primera llamada a la función con porcentaje de descuento por defecto (10%)
monto1 = 200  # Monto total de la compra
descuento1 = calcular_descuento(monto1)  # Llamada con porcentaje por defecto
monto_final1 = monto1 - descuento1  # Monto final a pagar después del descuento

# Segunda llamada a la función especificando el porcentaje de descuento (20%)
monto2 = 150  # Monto total de la compra
descuento2 = calcular_descuento(monto2, 20)  # Llamada con porcentaje específico
monto_final2 = monto2 - descuento2  # Monto final a pagar después del descuento

# Mostrando los resultados
print(f"Compra de ${monto1} con 10% de descuento:")
print(f"  Descuento aplicado: ${descuento1:.2f}")
print(f"  Monto final a pagar: ${monto_final1:.2f}\n")

print(f"Compra de ${monto2} con 20% de descuento:")
print(f"  Descuento aplicado: ${descuento2:.2f}")
print(f"  Monto final a pagar: ${monto_final2:.2f}")
