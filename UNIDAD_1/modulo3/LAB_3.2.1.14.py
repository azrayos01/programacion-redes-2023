""""
Nombre: Yazmin Elizabeth Rincon Ulloa
Descripcion: Utilizar el bucle while.
Encontrar la implementación adecuada de reglas definidas verbalmente.
Reflejar situaciones de la vida real en código de computadora.
Fecha: Domingo 15 de Octtubre del 2023
"""

blocks = int(input("Ingresa el número de bloques: "))

# Escribe tu código aquí.
height = 0
capa = 1

while blocks >= capa:
    height += 1
    blocks -= capa
    capa += 1

print("La altura de la pirámide:", height)
