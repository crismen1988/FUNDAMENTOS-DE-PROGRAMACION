# Libreria para generar numeros random
import random


# Definimos la funcion
def temperaturas(num_ciudad, num_semana, num_dia):
    # llamamos a la matriz de temperaturas
    matriz_temperaturas = [[[0 for _ in range(num_dia)] for _ in range(num_semana)] for _ in range(num_ciudad)]
    # recorremos la matriz en sus 3 dimensiones
    for i in range(num_ciudad):
        for j in range(num_semana):
            #ponemos a 0 la variable promedio
            resultado_temperaturas=0
            resultado_temperaturas = 0
            print(semanas[j].capitalize())
            for k in range(num_dia):
                # guardamos el numero random en la matruz
                matriz_temperaturas[i][j][k] = random.randint(15, 35)
                print(f"  {dias[k].capitalize()}: {matriz_temperaturas[i][j][k]} °C")
                # sumamos las temperaturas de cada dia
                resultado_temperaturas += matriz_temperaturas[i][j][k]
            # promediamos las temperaturas
            promedio_temperaturas_semana = resultado_temperaturas / num_dias
            # impresion del promedio
            print(f"  La media de Temperaturas de la {semanas[j]} en la ciudad de {ciudad.capitalize()} es: {promedio_temperaturas_semana:.2f} °C")
            print()


# definimos listas
ciudades = ["ambato", "quito", "cuenca"]
dias = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]
semanas = ["semana 1", "semana 2", "semana 3", "semana 4"]


# bucle para pedir varias veces la ciudad si el usuario asi lo desea
while True:
    # definimos variables para utilizar en el while
    condicional_semanas = True
    condicional_dias = True

    # impresion ciudades disponibles
    print("Ciudades disponibles para consultar: ")
    for num_ciudades in range(len(ciudades)):
        print(ciudades[num_ciudades].capitalize())
    # ingreso de la ciudad
    ciudad = input("Ingrese la Ciudad o 'S' para salir: ").lower()
    print()
    # salir del bucle por opcion del usuario
    if ciudad == "s":
        print("Hasta Pronto")
        break
    # by¿uscamos la ciudad ingresada en la lista de ciudades
    elif ciudad in ciudades:
        while condicional_semanas == True:
            # ingresamos el numero de semanas a consultar
            num_semanas = int(input("Ingrese el número de semanas 1-4: "))
            print()
            # verificacion del rango de semanas ingresado
            if num_semanas <= 4 and num_semanas != 0:
                while condicional_dias == True:
                    # ingresamos el numero de dias a consultar
                    num_dias = int(input("Ingrese el número de dias 1-7: "))
                    print()
                    # verificacion del rango de dias ingresado
                    if num_dias <= 7 and num_dias > 0:
                        temperaturas(1, num_semanas, num_dias)
                        # co
                        condicional_semanas = False
                        condicional_dias = False
                    else:
                        print("Número de dias incorrecto")
            else:
                print("Número de semanas incorrecto")
    else:
        print("Ciudad no encontrada")
        print()
