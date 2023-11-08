"""
Autor: Yazmin Elizabeth Rincon Ulloa
Descripcion: Un bucle for. El concepto de ejecución condicional (if-elif-else). La sentencia continue.
Fecha: Lunes 02 de Octubre del 2023
"""

user_word = input("Ingresa una palabra: ")

user_word = user_word.upper() 

for word in user_word:
    
    if word in "AEIOU":
        continue  
    print(word)