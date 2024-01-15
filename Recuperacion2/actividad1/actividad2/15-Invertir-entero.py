"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: Invertir un numero entero
"""

n = int(input("Ingrese un número entero: "))
if n < 0:
    signo = -1
    n = abs(n)
else:
    signo = 1
numero_invertido = 0
while n > 0:
    digito = n % 10
    numero_invertido = numero_invertido * 10 + digito
    n //= 10
numero_invertido *= signo
print("Número invertido:", numero_invertido)
