# Evaluación con letras A, B, C, D y F

calificacion = float(input("Ingresa tu calificación: "))

if calificacion >= 90:
    letra = "A"
elif calificacion >= 80:
    letra = "B"
elif calificacion >= 70:
    letra = "C"
elif calificacion >= 60:
    letra = "D"
else:
    letra = "F"

print("Tu calificación en letra es:", letra)