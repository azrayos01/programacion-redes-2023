"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: Suma de Digitos
"""
numero_usuario = input("Ingrese un número: ")

if numero_usuario.isdigit():
    suma = 0
    for digito in numero_usuario:
        suma += int(digito)

    print(f"La suma de los dígitos de {numero_usuario} es: {suma}")