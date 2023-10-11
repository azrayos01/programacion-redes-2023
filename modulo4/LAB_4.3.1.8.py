"""
Autor: Yazmin Elizabeth Rincon Ulloa
Descripcion: Utilizar la sentencia return.
Fecha: Lunes 02 de Octubre del 2023
"""

def is_year_leap(year):
#
# Tu código del LABORATORIO 4.3.1.6.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):
#
# Tu código del LABORATORIO 4.3.1.7.
    days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1 or month < 1 or month > 12:
        return None
    if month == 2 and is_year_leap(year):
        return 29
    return days_per_month[month]

def day_of_year(year, month, day):
#
# Escribe tu código nuevo aquí.
    if year < 1 or month < 1 or month > 12 or day < 1 or day > days_in_month(year, month):
        return None
    day_count = day
    for m in range(1, month):
        day_count += days_in_month(year, m)
    return day_count
#Impresion
print(day_of_year(2000, 12, 31))
