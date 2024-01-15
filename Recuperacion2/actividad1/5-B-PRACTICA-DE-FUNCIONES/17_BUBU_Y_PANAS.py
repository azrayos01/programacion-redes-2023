"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: Los Numeros de Missa (Facil)
"""
def es_capicua(numero):
    return str(numero) == str(numero)[::-1]

def capicua_repetida(numero):
    while not es_capicua(numero):
        numero += int(str(numero)[::-1])
    return numero
numero_ejemplo = int(input())
resultado = capicua_repetida(numero_ejemplo)
print(resultado)