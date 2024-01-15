"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: Domingo 07 de Enero de 2024
Descripcion: Par, Impar o Nulo
"""

A = int(input())

if A == 0:
    print("Nulo")
elif A % 2 == 0:
    print("Par")
else:
    print("Impar")