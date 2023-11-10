"""
Nombre: Yazmin Elizabeth Rincon Ulloa
Fecha:Viernes 10 de Noviembre del 2023
Descripcion: Mejorar las habilidades del estudiante para definir clases desde cero.
Emplear composición.
"""

import math

class Point:
    def __init__(self, x=0.0, y=0.0):
        self.__x = x
        self.__y = y

    def getx(self):
        return self.__x

    def gety(self):
        return self.__y

    def distance_from_point(self, point):
        return math.hypot(self.__x - point.getx(), self.__y - point.gety())

class Triangle:
    def __init__(self, point1, point2, point3):
        self.__points = [point1, point2, point3]

    def perimeter(self):
        side1 = self.__points[0].distance_from_point(self.__points[1])
        side2 = self.__points[1].distance_from_point(self.__points[2])
        side3 = self.__points[2].distance_from_point(self.__points[0])
        return side1 + side2 + side3

point1 = Point(0, 0)
point2 = Point(1, 1)
point3 = Point(2, 0)
triangle = Triangle(point1, point2, point3)
print(triangle.perimeter())  