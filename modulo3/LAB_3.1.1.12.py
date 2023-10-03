"""
Autor: Yazmin Elizabeth Rincon Ulloa
Descripcion: Familiarizarse con la sentencia if-else
Fecha: Lunes 02 de Octubre del 2023
"""

year = int(input("Introduce un año:"))

if year < 1582:
    print("No dentro del período del calendario Gregoriano")
else:
    if year % 4 != 0:
        print("Año comun")
    elif year % 100 != 0:
        print("Año bisiesto")
    else:
        print("Año bisiesto")
