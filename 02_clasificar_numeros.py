cantidad = int(input("¿Cuántos números vas a ingresar?: "))

mayores = 0
menores = 0
iguales = 0
contador = 1

while contador <= cantidad:
    numero = float(input(f"Ingresa el número {contador}: "))

    if numero > 0:
        mayores += 1
    elif numero < 0:
        menores += 1
    else:
        iguales += 1

    contador += 1

print("\nResultados:")
print("Mayores que cero:", mayores)
print("Menores que cero:", menores)
print("Iguales a cero:", iguales)