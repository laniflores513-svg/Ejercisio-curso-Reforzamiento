suma = 0
cantidad = 0

print("Ingresa números positivos.")
print("Ingresa un número negativo para terminar.")

while True:
    numero = float(input("Número: "))

    if numero < 0:
        break

    suma += numero
    cantidad += 1

if cantidad > 0:
    promedio = suma / cantidad
    print("La media de los números positivos es:", promedio)
else:
    print("No se ingresaron números positivos.")