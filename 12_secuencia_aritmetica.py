inicio = int(input("Ingresa el primer término: "))
diferencia = int(input("Ingresa la diferencia entre términos: "))
cantidad = int(input("¿Cuántos términos quieres generar?: "))

contador = 1
termino = inicio

if cantidad <= 0:
    print("La cantidad debe ser mayor que cero.")
else:
    print("Secuencia aritmética:")

    while True:
        print(termino)

        termino += diferencia
        contador += 1

        if contador > cantidad:
            break