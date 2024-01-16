"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: Lunes 15 de Enero de 2024
Descripcion: Velocidad Horizontal de un avión
"""

import math

def calcular_velocidad_promedio_aire(velocidad, angulo, direccion):
    if direccion == 0:  # Izquierda
        angulo = 180 - angulo

    # Convertir el ángulo a radianes
    angulo_radianes = math.radians(angulo)

    # Calcular la velocidad promedio del aire en el eje x
    velocidad_promedio = velocidad * math.cos(angulo_radianes)

    # Redondear el resultado hacia abajo
    velocidad_promedio = math.floor(velocidad_promedio)

    return velocidad_promedio

# Entrada de datos
try:
    entrada = input().strip().split(",")
    velocidad = int(entrada[0])
    angulo = int(entrada[1])
    direccion = int(entrada[2])

    # Calcular y mostrar la velocidad promedio del aire
    resultado = calcular_velocidad_promedio_aire(velocidad, angulo, direccion)
    print(resultado)
except ValueError:
    print("Entrada inválida. Asegúrate de ingresar números enteros.")
except IndexError:
    print("Entrada incompleta. Asegúrate de ingresar todos los valores necesarios.")
except Exception as e:
    print(f"Error inesperado: {e}")