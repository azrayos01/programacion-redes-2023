
"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: Cuadros vacios
"""

lado = int(input("Ingresa la medida del lado del cuadrado: "))

for i in range(lado):
    if i == 0 or i == lado - 1:
        print('* ' * lado)
    else:
        print('* ' + '  ' * (lado - 2) + '*')