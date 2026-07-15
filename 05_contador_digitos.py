numero = int(input("Ingresa un número entero: "))

numero = abs(numero)

if numero == 0:
    cantidad_digitos = 1
else:
    cantidad_digitos = 0

    while numero > 0:
        numero //= 10
        cantidad_digitos += 1

print("El número tiene", cantidad_digitos, "dígitos.")