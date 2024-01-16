"""
Autor: Rincon Ulloa Yazmin Elizabeth
Fecha: 15/01/2024
Descripcion: Los números de Zaido
"""

def suma_factores(n):
  suma = 0
  factor = 2
  while n > 1:
    potencia = 0
    while n % factor == 0:
      n = n // factor
      potencia += 1
    if potencia > 0:
      suma += factor ** potencia
    factor += 1 + factor % 2
  return suma

def es_zaido(n):
  return n % suma_factores(n) == 0

n = int(input())

if es_zaido(n):
  print("A wilson Zaido")
else:
  print("Chaaale")