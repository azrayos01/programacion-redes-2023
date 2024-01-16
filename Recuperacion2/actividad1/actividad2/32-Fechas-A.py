"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: Fechas A
"""

a, b, c = map(int, input().split())
es_bisiesto = (c % 4 == 0 and c % 100 != 0) or (c % 400 == 0)
dias_maximos = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if es_bisiesto:
    dias_maximos[2] = 29
if a < dias_maximos[b]:
    a += 1
else:
    a = 1
    if b < 12:
        b += 1
    else:
        b = 1
        c += 1
print(a, b, c)