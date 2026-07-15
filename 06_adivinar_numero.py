import random

numero_secreto = random.randint(1, 100)
intentos = 0
numero_usuario = 0

print("Adivina el número secreto entre 1 y 100.")

while numero_usuario != numero_secreto:
    numero_usuario = int(input("Ingresa tu intento: "))
    intentos += 1

    if numero_usuario < numero_secreto:
        print("El número secreto es mayor.")
    elif numero_usuario > numero_secreto:
        print("El número secreto es menor.")
    else:
        print("¡Correcto!")
        print("Número de intentos:", intentos)