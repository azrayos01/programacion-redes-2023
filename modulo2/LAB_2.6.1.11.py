"""
Autor: Yazmin Elizabeth Rincon Ulloa
Descripcion: Uso de la funcion print() y sus capacidades.
Fecha: Lunes 02 de Octubre del 2023
"""

hora = int(input("Hora de inicio (horas): "))
minutos = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# Escribe tu código aqui.
minutost = hora * 60 + minutos + dura
finalh = minutost // 60
finalm = minutost % 60
finalh = finalh % 24

print(f"Termina a las {finalh:02}:{finalm:02}")
