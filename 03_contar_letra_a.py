palabra = input("Ingresa una palabra: ").lower()

contador_a = 0
posicion = 0

while posicion < len(palabra):
    if palabra[posicion] == "a":
        contador_a += 1

    posicion += 1

print("La palabra contiene", contador_a, "letras 'a'.")