#Ejercicio 3
#Diseñar el algoritmo correspondiente a un programa, que:
#Crea una tabla bidimensional de longitud 5x5 y nombre 'matriz'. Carga la tabla con valores numéricos enteros.
#Suma todos los elementos de cada fila y todos los elementos de cada columna visualizando los resultados en pantalla.

# Crear la matriz 5x5
matriz = [[0 for _ in range(5)] for _ in range(5)]

# Cargar los valores ingresados por el usuario
for i in range(5):
    for j in range(5):
        matriz[i][j] = int(input(f"Ingresa el valor para matriz: "))
# Sumar filas y mostrar resultados
for i in range(5):
    suma_fila = 0
    for j in range(5):
        suma_fila += matriz[i][j]
    print(f"Suma de la fila {i + 1} es: {suma_fila}")
1
# Sumar columnas y mostrar resultados
for j in range(5):
    suma_columna = 0
    for i in range(5):
        suma_columna += matriz[i][j]
    print(f"Suma de la columna {j + 1} es: {suma_columna}")