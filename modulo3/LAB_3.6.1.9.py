""""
Nombre: Yazmin Elizabeth Rincon Ulloa
Descripcion: Indexación de listas.
Utilizar operadoresin y not in.
Fecha: Domingo 15 de Octtubre del 2023
"""

my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

# Escribe tu código aquí.

lista = []

for i in my_list:
    if i not in lista:
        lista.append(i)

print("La lista con elementos únicos:")
print(lista)