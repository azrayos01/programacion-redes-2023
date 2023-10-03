"""
Autor: Yazmin Elizabeth Rincon Ulloa
Descripcion: Familiarizarse con la sentencia if-else
Fecha: Lunes 02 de Octubre del 2023
"""

income = float(input("Introduce el ingreso anual:"))

if income <= 85528:
    tax = income * 0.18 - 556.02
else:
    tax = 14839.02 +  0.32 * (income - 85528)

tax = max(0, tax)
tax = round(tax)

print("El impuesto es:", tax, "pesos")