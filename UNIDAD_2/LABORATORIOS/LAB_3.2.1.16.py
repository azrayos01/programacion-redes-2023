"""
Nombre: Yazmin Elizabeth Rincon Ulloa
Fecha:Viernes 10 de Noviembre del 2023
Descripcion:Mejorar las habilidades del estudiante para definir subclases.
Agregar nueva funcionalidad a una clase existente.
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
            raise QueueError("Cola vacia")  
        return self.items.pop()  
    def is_empty(self):
        return not bool(self.items)  

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

print(q.is_empty()) 