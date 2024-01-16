"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: Encriptando el mensaje
"""
palabra1 = input()
palabra2 = input()
mensaje_encriptado = ""
for char1, char2 in zip(palabra1, palabra2):
    mensaje_encriptado += char1 + char2
print(mensaje_encriptado)
