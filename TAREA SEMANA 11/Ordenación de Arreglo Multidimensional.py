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
    [12, 25, 18],  # Segunda fila
    [22, 3, 15]  # Tercera fila
]

# Inicializamos el contador de Intentos
contador = 0
while contador < 3:
    # Calculamos la longitud de la matriz
    longitud_matriz = len(matriz)
    print(f"Esta Matriz contiene {longitud_matriz} Fila")
    print(" ")
    # Se ingresa el numero de fila que se desea ordenar
    fila_usuario = input("Ingrese el número de la fila que desea ordenar: ")
    print(" ")
    # Verificamos que el dato ingresado sea un numero y este dentro del rango del
    # número de filas de la matriz
    if fila_usuario.isdigit() and (int(fila_usuario) <= longitud_matriz and int(fila_usuario) != 0):
        fila_usuario = int(fila_usuario)
        indice_fila = fila_usuario - 1
        # Imprimimos la matriz original
        print("MATRIZ ORIGINAL")
        imprimir_matriz(matriz)
        print(" ")
        # Imprimimos la matriz ordenada
        print("MATRIZ ORDENADA")
        ordenar_fila(matriz, indice_fila)
        imprimir_matriz(matriz)
        print(" ")
        break
    else:
        # Dato Ingresado incorrecto el contador aumenta y los intentos disminuyen
        print("Dato Ingresado Incorrecto o Fuera de rango de la longitud de la Matriz")
        print(" ")
        contador += 1
        print(f"Le quedan {3 - contador} Intentos")
        print(" ")
