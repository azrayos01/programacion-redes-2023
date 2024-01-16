"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: Gasolina Magna
"""
costo_gasolina = 19.03

incremento_mensual = 0.02
incremento_semestral = 0.28
incremento_anual = 1.011
descuento_sexenal = 1.99

meses = int(input("Ingrese el número de meses: "))
for mes in range(1, meses + 1):
    costo_gasolina += incremento_mensual
    if mes % 6 == 0:
        costo_gasolina += incremento_semestral
    if mes % 12 == 0:
        costo_gasolina *= incremento_anual
    if mes % 72 == 0:
        costo_gasolina -= descuento_sexenal
print(f"El costo final de la gasolina Magna después de {meses} meses es: ${costo_gasolina:.2f}")