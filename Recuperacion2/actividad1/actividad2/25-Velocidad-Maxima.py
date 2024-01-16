"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: Velocidad maxima
"""
n = int(input())

velocidad_maxima = 0

for _ in range(n):
    km_recorridos, horas_transcurridas = map(float, input().split())
    velocidad_actual = km_recorridos / horas_transcurridas
    if velocidad_actual > velocidad_maxima:
        velocidad_maxima = velocidad_actual

print(velocidad_maxima)
