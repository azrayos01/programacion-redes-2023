""""
Nombre: Yazmin Elizabeth Rincon Ulloa
Descripcion: Utilizar la instrucción continue en los bucles.
Modificar y actualizar el código existente.
Reflejar situaciones de la vida real en código de computadora.
Fecha: Domingo 15 de Octtubre del 2023
"""

word_without_vowels = ""

# Indicar al usuario que ingrese una palabra
# y asignarla a la variable user_word.
user_word = input("Ingrese una palabra: ")
user_word = user_word.upper()

for letter in user_word:
    # Completa el cuerpo del bucle.
    if letter in "AEIOU":
        continue
    word_without_vowels += letter

# Imprimir la palabra asignada a word_without_vowels.
print("Palabra: ", word_without_vowels)