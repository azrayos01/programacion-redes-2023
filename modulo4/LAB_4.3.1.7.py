"""
Autor: Yazmin Elizabeth Rincon Ulloa
Descripcion: Utilizar la sentencia return.
Fecha: Lunes 02 de Octubre del 2023
"""

def is_year_leap(year):

# Tu código del LABORATORIO 4.3.6.
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

def days_in_month(year, month):

# Escribe tu código aquí.
    days_per_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if year < 1 or month < 1 or month > 12:
        return None
    if month == 2 and is_year_leap(year):
        return 29
    return days_per_month[month]

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 1, 11]
test_results = [28, 29, 31, 30]
for i in range(len(test_years)):
	yr = test_years[i]
	mo = test_months[i]
	print(yr, mo, "->", end="")
	result = days_in_month(yr, mo)
	if result == test_results[i]:
		print("OK")
	else:
		print("Fallido")
