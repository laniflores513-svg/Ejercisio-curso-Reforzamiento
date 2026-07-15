# Determinar estación del año usando match-case

mes = input("Ingresa un mes: ").lower()

match mes:
    case "marzo" | "abril" | "mayo":
        estacion = "Primavera"

    case "junio" | "julio" | "agosto":
        estacion = "Verano"

    case "septiembre" | "octubre" | "noviembre":
        estacion = "Otoño"

    case "diciembre" | "enero" | "febrero":
        estacion = "Invierno"

    case _:
        estacion = None
        print("El mes ingresado no es válido.")

if estacion is not None:
    print("La estación es:", estacion)