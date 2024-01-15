
"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: Domingo 07 de Enero de 2024
Descripcion: Edades
""" 

numero_alumnos = int(input())

edades = list(map(int, input().split()))

edades_frecuencia = [(edad, edades.count(edad)) for edad in set(edades)]

edades_frecuencia.sort()

for edad, frecuencia in edades_frecuencia:
    print(f"{edad} {frecuencia}")