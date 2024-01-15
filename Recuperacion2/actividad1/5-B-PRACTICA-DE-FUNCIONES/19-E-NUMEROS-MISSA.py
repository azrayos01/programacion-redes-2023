"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: Los Numeros de Missa
"""
def grado_missa(numero):
    n = 1
    while True:
        suma_digitos = sum(int(digito) ** n for digito in str(numero))
        if suma_digitos == numero:
            return n
        elif suma_digitos > numero:
            return -1
        n += 1
numero_ejemplo = int(input())
resultado = grado_missa(numero_ejemplo)
print(resultado)