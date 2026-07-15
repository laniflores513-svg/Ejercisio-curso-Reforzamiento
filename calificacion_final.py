# Calificación final:
# Parciales 40%, proyecto 30% y examen 30%

parciales = float(input("Calificación de parciales: "))
proyecto = float(input("Calificación del proyecto: "))
examen = float(input("Calificación del examen: "))

calificacion_final = (
    parciales * 0.40
    + proyecto * 0.30
    + examen * 0.30
)

print("La calificación final es:", round(calificacion_final, 2))