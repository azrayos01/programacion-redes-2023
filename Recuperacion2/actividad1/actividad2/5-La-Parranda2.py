"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: La Parranda 2
"""
n = int(input())
mitad_tragos = n // 2
if n % 2 == 0 and n > 0:
    print(mitad_tragos)
else:
    print(0)
