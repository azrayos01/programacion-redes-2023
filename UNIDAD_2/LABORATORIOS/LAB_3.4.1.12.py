"""
Nombre: Yazmin Elizabeth Rincon Ulloa
Fecha:Viernes 10 de Noviembre del 2023
Descripcion:Mejorar las habilidades del estudiante para definir clases desde cero.
Definir y usar variables de instancia.
Definir y usar métodos.
"""

class Timer:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.__hours = hours
        self.__minutes = minutes
        self.__seconds = seconds

    def __str__(self):
        return self.format_time()

    def format_time(self):
        return f'{self.__hours:02}:{self.__minutes:02}:{self.__seconds:02}'

    def next_second(self):
        self.__seconds += 1
        if self.__seconds == 60:
            self.__seconds = 0
            self.__minutes += 1
            if self.__minutes == 60:
                self.__minutes = 0
                self.__hours += 1
                if self.__hours == 24:
                    self.__hours = 0

    def previous_second(self):
        self.__seconds -= 1
        if self.__seconds == -1:
            self.__seconds = 59
            self.__minutes -= 1
            if self.__minutes == -1:
                self.__minutes = 59
                self.__hours -= 1
                if self.__hours == -1:
                    self.__hours = 23

timer1 = Timer(23, 59, 59)
print(timer1)  

timer1.next_second()
print(timer1)  

timer1.previous_second()
print(timer1)  