cantidad = int(input("¿Cuántos números vas a ingresar?: "))

contador = 0
impares = 0

if cantidad <= 0:
    print("La cantidad debe ser mayor que cero.")
else:
    while True:
        numero = int(input(f"Ingresa el número {contador + 1}: "))

        if numero % 2 != 0:
            impares += 1

        contador += 1

        if contador >= cantidad:
            break

    print("Cantidad de números impares:", impares)