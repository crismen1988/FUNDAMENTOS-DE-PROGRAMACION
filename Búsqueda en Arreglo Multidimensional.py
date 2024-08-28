matriz=[
    [1,2,3],
    [4,9,6],
    [7,8,5],
]
elemento_a_buscar = 5

# Buscar el elemento en la lista 3x3
encontrado = False  # verifica si el elemento se encuentra
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        if matriz[i][j] == elemento_a_buscar:
            print(f"El elemento {elemento_a_buscar} se encuentra en el índice [{i}][{j}]")
            encontrado = True
            break
# Si no se encuentra el elemento
if encontrado==False:
    print(f"El elemento {elemento_a_buscar} no se encuentra en la lista.")

