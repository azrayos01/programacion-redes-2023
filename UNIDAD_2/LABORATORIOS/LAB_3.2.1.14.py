"""
Nombre: Yazmin Elizabeth Rincon Ulloa
Fecha:Viernes 10 de Noviembre del 2023
Descripcion: Mejorar las habilidades del estudiante para definir clases.
Emplear clases existentes para crear nuevas clases equipadas con nuevas funcionalidades.
"""

class Stack:
    def __init__(self):
        self.__stk = []

    def push(self, val):
        self.__stk.append(val)

    def pop(self):
        val = self.__stk[-1]
        del self.__stk[-1]
        return val

class CountingStack(Stack):
    def __init__(self):
        super().__init__()  
        self.__counter = 0  

    def get_counter(self):
        return self.__counter  

    def pop(self):
        val = super().pop()  
        self.__counter += 1  
        return val

stk = CountingStack()
for i in range(100):
    stk.push(i)
    stk.pop()

print(stk.get_counter())  