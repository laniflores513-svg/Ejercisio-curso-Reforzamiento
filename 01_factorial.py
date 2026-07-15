numero = int(input("Ingresa un número entero positivo: "))

if numero < 0:
    print("No existe el factorial de un número negativo.")
else:
    factorial = 1
    contador = 1

    while contador <= numero:
        factorial *= contador
        contador += 1

    print("El factorial de", numero, "es:", factorial)