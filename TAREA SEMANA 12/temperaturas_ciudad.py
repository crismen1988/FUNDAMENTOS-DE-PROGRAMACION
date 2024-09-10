#Importar la libreria para generar un numero random
import random
#Definir el numero de ciudades, dias y semanas
ciudad=3
dia=7
semana=4
#Crear listas para en ellas definir un banco de ciudades, semanas y dias
ciudades=["Ambato","Quito","Cuenca"]
semanas=["Semana 1","Semana 2","Semana 3","Semana 4"]
dias=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

#LLamamos a la matriz
matriz_temperaturas = [[[0 for _ in range(dia)] for _ in range(semana)] for _ in range(ciudad)]
#Establecemos un bucle para recorrer la matriz
for i in range (ciudad):
    #Impresion del nombre de la ciudad
    print(f"\033[92m{ciudades[i]}")
    for j in range(semana):
        #Enceramos las variables de promedio y suma de temperaturas
        promedio=0
        suma_temperaturas=0
        #Imprimimos la semana que corresponde
        print(f"\033[93m{semanas[j]}")
        for k in range(dia):
            #Generamos un numero random
            temperatura=random.randint(15, 35)
            #Ingresamos el numero random en la matriz
            matriz_temperaturas[i][j][k]=temperatura
            #Impresion de la temperatura diaria
            print(f"  \033[97m{dias[k]} = {matriz_temperaturas[i][j][k]} °C")
            #Suma de temperaturas diarias
            suma_temperaturas+=matriz_temperaturas[i][j][k]
        #Promediamos las temperaturas
        promedio=suma_temperaturas/dia
        #Imprimimos el promedio de temperaturas
        print(f"  \033[96mEl promedio de temperatura de la {semanas[j].lower()} en la ciudad de {ciudades[i]} es: \033[97m{promedio:.2f} °C\n")