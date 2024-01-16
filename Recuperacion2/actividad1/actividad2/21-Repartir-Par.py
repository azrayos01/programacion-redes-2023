"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: Repartir Par
"""
total_manzanas = int(input())
num_hermanas = int(input())

manzanas_por_hermana = total_manzanas // num_hermanas

if manzanas_por_hermana % 2 == 0 and manzanas_por_hermana > 0:
    print(manzanas_por_hermana)
else:
    print("NO")
