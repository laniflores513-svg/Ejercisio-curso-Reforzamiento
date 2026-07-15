numero = 1

print("Números divisibles entre 3 y 5:")

while numero <= 100:
    if numero % 3 == 0 and numero % 5 == 0:
        print(numero)

    numero += 1