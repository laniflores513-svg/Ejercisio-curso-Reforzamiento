# Conversor de pesos mexicanos a otras monedas

pesos = float(input("Cantidad en pesos mexicanos: $"))

print("1. USD - Dólar estadounidense")
print("2. EUR - Euro")
print("3. THB - Baht tailandés")
print("4. JPY - Yen japonés")
print("5. KRW - Won surcoreano")
print("6. AUD - Dólar australiano")
print("7. PEN - Sol peruano")
print("8. CAD - Dólar canadiense")
print("9. VES - Bolívar venezolano")
print("10. ARS - Peso argentino")

opcion = int(input("Elige una moneda: "))

match opcion:
    case 1:
        resultado = pesos * 0.055
        moneda = "USD"

    case 2:
        resultado = pesos * 0.051
        moneda = "EUR"

    case 3:
        resultado = pesos * 1.95
        moneda = "THB"

    case 4:
        resultado = pesos * 8.50
        moneda = "JPY"

    case 5:
        resultado = pesos * 75
        moneda = "KRW"

    case 6:
        resultado = pesos * 0.083
        moneda = "AUD"

    case 7:
        resultado = pesos * 0.21
        moneda = "PEN"

    case 8:
        resultado = pesos * 0.075
        moneda = "CAD"

    case 9:
        resultado = pesos * 2.00
        moneda = "VES"

    case 10:
        resultado = pesos * 55
        moneda = "ARS"

    case _:
        resultado = None
        print("Opción inválida.")

if resultado is not None:
    print("Cantidad convertida:", round(resultado, 2), moneda)