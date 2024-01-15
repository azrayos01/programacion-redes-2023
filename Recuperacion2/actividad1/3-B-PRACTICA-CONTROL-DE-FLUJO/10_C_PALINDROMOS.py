"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: Domingo 07 de Enero de 2024
Descripcion: Palabra palindroma
"""
p = input()

if p == p[::-1]:
    print("SI")
else:
    print("NO")