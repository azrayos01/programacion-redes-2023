"""
Autor: Yazmin Elizabeth Rincón Ulloa 
Fecha de creación: Lunes 02 de Octubre del 2023
unidad1_modulo2
Ejercicio practico 2
"""

asignaturas = ["Probabilidad", "Electronica", "Conexiones", "Servidores", "Programacion", "Ingles"]
notas = []
for asignatura in asignaturas:
    nota = float(input(f"Dame la nota de la unidad I en {asignatura}: "))
    notas.append((asignatura, nota))

for asignatura, nota in notas:
    print(f"En {asignatura} has sacado {nota}")