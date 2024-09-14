#Definimos elementos de la matriz
matriz=[
    [1,2,3],
    [4,9,6],
    [7,8,5]
]
#Se pide al usuario ingresar el valor que desea buscar
elemento_a_buscar= int(input("Ingrese el Valor a buscar dentro de la matriz, debe ser un número entero: "))
# Buscar el elemento en la lista 3x3
encontrado = False  # verifica si el elemento se encuentra
for fila in range(len(matriz)):
    for columna in range(len(matriz[fila])):
        #Si el elemento se encuentra dentro de la matriz
        if matriz[fila][columna] == elemento_a_buscar:
            print(f"El elemento {elemento_a_buscar} se encuentra en el índice [{fila}][{columna}]")
            encontrado = True
            break
# Si no se encuentra el elemento
if encontrado==False:
    print(f"El elemento {elemento_a_buscar} no se encuentra en la lista.")
