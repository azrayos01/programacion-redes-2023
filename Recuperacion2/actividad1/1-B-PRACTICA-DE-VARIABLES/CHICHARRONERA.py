"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: Sabado 06 de Enero de 2024
Descripcion: Hola Mundo
"""

a, b, c = map(int, input().split())

discriminante = b**2 - 4*a*c

if discriminante >= 0:
    raiz_cuadrada = discriminante**0.5
    x1 = (-b + raiz_cuadrada) / (2*a)
    x2 = (-b - raiz_cuadrada) / (2*a)
    
    print(f"{x1:.6f} {x2:.6f}")
else:
    print("No hay soluciones reales para la ecuación cuadrática dada.")