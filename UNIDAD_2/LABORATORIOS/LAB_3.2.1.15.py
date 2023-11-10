"""
Nombre: Yazmin Elizabeth Rincon Ulloa
Fecha:Viernes 10 de Noviembre del 2023
Descripcion:Mejorar las habilidades del estudiante para definir clases desde cero.
Implementar estructuras de datos estándar como clases.
"""

class QueueError(Exception):
    pass

class Queue:
    def __init__(self):
        self.items = []

    def put(self, item):
        self.items.insert(0, item)  

    def get(self):
        if not self.items:
            raise QueueError("Error de Cola")  
        return self.items.pop()  
    
q = Queue()
q.put(1)
q.put("perro")
q.put(False)

try:
    print(q.get())  
    print(q.get())  
    print(q.get())  
    print(q.get())  
except QueueError as e:
    print(e) 