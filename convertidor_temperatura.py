# Convertidor de Celsius a Fahrenheit o Kelvin

celsius = float(input("Temperatura en grados Celsius: "))

print("1. Convertir a Fahrenheit")
print("2. Convertir a Kelvin")

opcion = int(input("Elige una opción: "))

match opcion:
    case 1:
        resultado = celsius * 9 / 5 + 32
        unidad = "°F"

    case 2:
        resultado = celsius + 273.15
        unidad = "K"

    case _:
        resultado = None
        print("Opción inválida.")

if resultado is not None:
    print("Temperatura convertida:", round(resultado, 2), unidad)