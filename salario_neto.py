# Salario neto

salario_bruto = 15000
impuestos = 16
deducciones = 5

total_descuentos = (impuestos + deducciones) / 100
salario_neto = salario_bruto - (salario_bruto * total_descuentos)

print("Salario bruto:", salario_bruto)
print("Impuestos:", impuestos, "%")
print("Deducciones:", deducciones, "%")
print("Salario neto:", salario_neto)