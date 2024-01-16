"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: Palindrome
"""
numero = int(input("Ingrese un número de 3 dígitos (000-999): "))

if 0 <= numero <= 999:
    str_numero = str(numero)
    
    if str_numero[0] == str_numero[2]:
        print("Verdadero")
    else:
        print("Falso")