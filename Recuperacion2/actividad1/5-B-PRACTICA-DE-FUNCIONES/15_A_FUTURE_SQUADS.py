
def factorial(n):
    return 1 if n == 0 or n == 1 else n * factorial(n-1)
nombres = [nombre for nombre in input().split() if nombre not in ["Ricardo", "Mirón"]]
num_personas = len(nombres)
print(0 if num_personas < 4 else factorial(num_personas) // (factorial(num_personas-4) * factorial(4)))