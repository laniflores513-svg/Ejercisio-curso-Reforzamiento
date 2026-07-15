while True:
    print("\n--- CALCULADORA BÁSICA ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Salir")

    opcion = input("Selecciona una opción: ")

    if opcion == "5":
        print("Calculadora finalizada.")
        break

    if opcion in ["1", "2", "3", "4"]:
        numero1 = float(input("Ingresa el primer número: "))
        numero2 = float(input("Ingresa el segundo número: "))

        if opcion == "1":
            resultado = numero1 + numero2
            print("Resultado:", resultado)

        elif opcion == "2":
            resultado = numero1 - numero2
            print("Resultado:", resultado)

        elif opcion == "3":
            resultado = numero1 * numero2
            print("Resultado:", resultado)

        elif opcion == "4":
            if numero2 != 0:
                resultado = numero1 / numero2
                print("Resultado:", resultado)
            else:
                print("No se puede dividir entre cero.")
    else:
        print("Opción incorrecta.")