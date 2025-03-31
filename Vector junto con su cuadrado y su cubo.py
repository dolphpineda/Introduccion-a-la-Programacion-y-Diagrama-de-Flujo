#Ejercicio 1 de Vectores y Matrices
#Realizar un programa que defina un vector llamado "vector_numeros" de 10 enteros, a continuación lo inicialice con valores 
# aleatorios (del 1 al 10) y posteriormente muestre en pantalla cada elemento del vector junto con su cuadrado y su cubo.

import random

# Definir el vector de 10 enteros
vector_numeros = [0] * 10

# Inicializar el vector con valores aleatorios del 1 al 10
for i in range(10):
    vector_numeros[i] = random.randint(1, 10)

# Numero aleatorios elevados al cuadrado y al cubo
print("Elemento | Cuadrado | Cubo")
print("--------------------------")
for elemento in vector_numeros:
    cuadrado = elemento ** 2
    cubo = elemento ** 3
    print(f"{elemento:^8} | {cuadrado:^7} | {cubo:^6}")