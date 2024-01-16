"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: Lunes 15 de Enero de 2024
Descripcion: Edades y cluberos
"""
edades = input().split()
conjunto_edades = set(edades)
lista_edades_ordenada = sorted(conjunto_edades, reverse=True)
print(lista_edades_ordenada)