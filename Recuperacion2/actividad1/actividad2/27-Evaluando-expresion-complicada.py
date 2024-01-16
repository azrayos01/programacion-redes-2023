"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: Evaluando una expresión complicada
"""

x = float(input("Ingresa el valor de x: "))
y = float(input("Ingresa el valor de y: "))
z = float(input("Ingresa el valor de z: "))

resultado = ((2 * y + z) ** 2.8 - z) / (x + y - (x / z))

print(f"El resultado de la expresión es: {resultado}")