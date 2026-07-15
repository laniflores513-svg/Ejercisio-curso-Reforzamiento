vocales = 0
consonantes = 0

print("Ingresa letras una por una.")
print("Presiona Enter para terminar.")

while True:
    letra = input("Ingresa una letra: ")

    if letra == "":
        break

    letra = letra.lower()

    if len(letra) != 1 or not letra.isalpha():
        print("Debes ingresar solamente una letra.")
    elif letra in "aeiou":
        vocales += 1
    else:
        consonantes += 1

print("\nResultados:")
print("Vocales:", vocales)
print("Consonantes:", consonantes)