""""
Nombre: Yazmin Elizabeth Rincon Ulloa
Descripcion: Utilizar el bucle while.
Reflejar situaciones de la vida real en código de computadora.
Fecha: Domingo 15 de Octtubre del 2023
"""

secret_number = 777

print(
"""
+==================================+
| ¡Bienvenido a mi juego, muggle!  |
| Introduce un número entero       |
| y adivina qué número he          |
| elegido para ti.                 |
| Entonces,                        |
| ¿Cuál es el número secreto?      |
+==================================+
""")
number = int(input())

while (number != secret_number):
    print("¡Ja, ja! ¡Estás atrapado en mi bucle!")
    number = int(input())

print("¡Bien hecho, muggle! Eres libre ahora")