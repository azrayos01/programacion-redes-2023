"""
Autor: Yazmin Elizabeth Rincon Ulloa
Descripcion: Familiarizar al estudiante con nociones y algoritmos clásicos.
Mejorar las habilidades del estudiante para definir y emplear funciones
Fecha: Jueves 12 de Octubre del 2023
"""

def is_prime(num):
#
# Escribe tu código aquí.
    if num <= 1:
        return False
    if num == 2:
        return True
    if num % 2 == 0:
        return False
    for i in range(3, int(num**0.5) + 1, 2):
        if num % i == 0:
            return False
    return True
#Prueba
for i in range(1, 20):
	if is_prime(i + 1):
			print(i + 1, end=" ")
print()