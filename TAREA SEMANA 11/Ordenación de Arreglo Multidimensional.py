# Función para ordenar una fila de la matriz usando la función sorted()
def ordenar_fila(matriz, indice_fila):
    # Ordenamos la fila usando la función sorted() y la reemplazamos en la matriz
    matriz[indice_fila] = sorted(matriz[indice_fila])

# Función para imprimir la matriz
def imprimir_matriz(matriz):
    for fila in matriz:
        print(fila)

# Matriz 3x3 inicial
matriz = [
    [34, 8, 50],  # Primera fila
    [12, 25, 18], # Segunda fila
    [22, 3, 15]   # Tercera fila
]

#Se ingresa el numero de fila que se desea ordenar
indice=int(input("Ingrese el número de la fila que desea ordenar: "))
#Le restamos uno al dato ingresado por el usuario
#El usuario no sabe que los indices comienzan desde cero
indice=indice-1

# Mostramos la matriz original
print("Matriz original:")
imprimir_matriz(matriz)

# Ordenamos la segunda fila (índice)
ordenar_fila(matriz, indice)

# Mostramos la matriz después de ordenar la fila
print("\nMatriz con la segunda fila ordenada:")
imprimir_matriz(matriz)