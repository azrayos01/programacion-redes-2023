""""
Nombre: Yazmin Elizabeth Rincon Ulloa
Descripcion: Utilizar el bucle while.
Convertir bucles definidos verbalmente en código real de Python.
Fecha: Domingo 15 de Octtubre del 2023
"""

c0 = int(input("Ingresa un número natural: "))
pasos = 0

print("Valores intermedios:")

while c0 != 1:
    print(c0)
    if c0 % 2 == 0:
        c0 = c0 // 2
    else:
        c0 = 3 * c0 + 1
    pasos += 1

print(1)
print("Se necesitaron", pasos, "pasos para alcanzar 1.")