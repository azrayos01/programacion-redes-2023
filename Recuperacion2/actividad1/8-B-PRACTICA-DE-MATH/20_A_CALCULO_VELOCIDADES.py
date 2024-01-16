"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion:  Cálculo de velocidades en Future Lab
"""

import math

def calcular_velocidad_promedio(fuerza_levantamiento, densidad_aire, coeficiente_levantamiento, superficie_alar):
    velocidad = math.sqrt((2 * fuerza_levantamiento) / (densidad_aire * coeficiente_levantamiento * superficie_alar))
    return velocidad

def main():
    sets = input().strip().split()

    velocidades = []

    for set_parametros in sets:
        parametros = list(map(float, set_parametros.split(',')))

        velocidad = calcular_velocidad_promedio(*parametros)

        velocidades.append(velocidad)

    velocidad_promedio = math.ceil(math.fsum(velocidades) / len(velocidades))

    print(velocidad_promedio)

if __name__ == "__main__":
    main()