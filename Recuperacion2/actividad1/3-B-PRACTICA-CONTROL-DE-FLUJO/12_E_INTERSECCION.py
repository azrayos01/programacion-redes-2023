"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: Sabado 07 de Enero de 2024
Descripcion: Intersección de intervalos
"""

a, b, c, d = map(int, input().split())

if c <= b and a <= d:
    print(1)
else:
    print(0)


