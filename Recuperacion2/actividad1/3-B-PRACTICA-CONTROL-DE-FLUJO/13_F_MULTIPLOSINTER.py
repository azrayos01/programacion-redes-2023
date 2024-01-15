"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: Domingo 07 de Enero de 2024
Descripcion: Multiplos dentro de un intervalo
"""
a, b = map(int, input().split())

for numero in range(a, b + 1, a):
    print(numero, end=' ')