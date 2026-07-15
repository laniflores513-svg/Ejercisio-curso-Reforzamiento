# Calcular precio con descuento

precio = float(input("Ingresa el precio del producto: $"))

if precio <= 100:
    descuento = 0.05
elif precio <= 200:
    descuento = 0.10
elif precio <= 500:
    descuento = 0.15
else:
    descuento = 0.20

cantidad_descuento = precio * descuento
precio_final = precio - cantidad_descuento

print("Descuento:", descuento * 100, "%")
print("Cantidad descontada: $", round(cantidad_descuento, 2))
print("Precio final: $", round(precio_final, 2))