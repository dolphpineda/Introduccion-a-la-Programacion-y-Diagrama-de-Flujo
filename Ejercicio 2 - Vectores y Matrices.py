 #Ejercicio 2 - Vectores y Matrices
#Crear un vector de 5 elementos de cadenas de caracteres, inicializa el vector con datos leídos por el teclado. 
# Copia los elementos del vector en otro vector pero en orden inverso, y muéstralo por la pantalla.

# Crear un vector de 5 cadenas 
vector_original = []

# Inicializar el vector con datos leídos por el teclado
for i in range(5):
    cadena = input(f"Ingresa la cadena {i +1}: ")
    vector_original.append(cadena)

# Copiar los elementos reordenados inversos
vector_inverso = vector_original[::-1]

# Mostrar el vector inverso
print("\Vector en orden inverso:")
for cadena in vector_inverso:
    print(cadena)