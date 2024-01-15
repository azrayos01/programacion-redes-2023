"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: Domingo 07 de Enero de 2024
Descripcion: Operaciones con Strings
"""
cadena = input().strip().split()

for i, palabra in enumerate(cadena):
    if i % 2 == 0:
        print(palabra.lower(), end=" ")
    else:
        print(palabra.upper(), end=" ")