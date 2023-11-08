""""
Nombre: Yazmin Elizabeth Rincon Ulloa
Descripcion: Crear y modificar listas simples.
Utilizar métodos para modificar listas.
Fecha: Domingo 15 de Octtubre del 2023
"""

# paso 1
Beatles = []
print("Paso 1:", Beatles)

# paso 2
Beatles.append ("John Lennon")
Beatles.append ("Paul McCartney")
Beatles.append ("George Harrison")
print("Paso 2:", Beatles)

# paso 3
miembro = 0
for i in range(2):
    miembro = input("Agrega a los integrantes faltantes: ")
    Beatles.append(miembro)
print("Paso 3:", Beatles)

# paso 4
del Beatles[3]
del Beatles[3]
print("Paso 4:", Beatles)

# paso 5
Beatles.insert(0, "Ringo Starr")
print("Paso 5:", Beatles)
