cantidad = int(input("¿Cuántos cuadrados quieres generar?: "))

numero = 1

if cantidad <= 0:
    print("La cantidad debe ser mayor que cero.")
else:
    while True:
        cuadrado = numero ** 2
        print(numero, "al cuadrado es", cuadrado)

        numero += 1

        if numero > cantidad:
            break