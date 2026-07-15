# Información sobre artistas, películas y series

print("1. Shakira")
print("2. Luis Miguel")
print("3. Titanic")
print("4. Spider-Man")
print("5. Stranger Things")
print("6. Cobra Kai")
print("7. Toy Story")

opcion = int(input("Elige una opción: "))

match opcion:
    case 1:
        print("Shakira es una cantante y compositora colombiana.")

    case 2:
        print("Luis Miguel es un cantante mexicano conocido como El Sol de México.")

    case 3:
        print("Titanic es una película dramática estrenada en 1997.")

    case 4:
        print("Spider-Man es un superhéroe que aparece en películas y cómics.")

    case 5:
        print("Stranger Things es una serie de ciencia ficción y misterio.")

    case 6:
        print("Cobra Kai es una serie basada en la historia de Karate Kid.")

    case 7:
        print("Toy Story es una película animada sobre juguetes que cobran vida.")

    case _:
        print("Opción inválida.")