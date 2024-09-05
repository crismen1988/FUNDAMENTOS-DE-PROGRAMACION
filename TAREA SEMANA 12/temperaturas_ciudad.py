import random
ciudad=3
dia=7
semana=4
ciudades=["Ambato","Quito","Cuenca"]
semanas=["Semana 1","Semana 2","Semana 3","Semana 4"]
dias=["Lunes","Martes","Miércoles","Jueves","Viernes","Sábado","Domingo"]

matriz_temperaturas = [[[0 for _ in range(dia)] for _ in range(semana)] for _ in range(ciudad)]

for i in range (ciudad):
    print(f"\033[92m{ciudades[i]}")
    for j in range(semana):
        promedio=0
        suma_temperaturas=0
        print(f"\033[93m{semanas[j]}")
        for k in range(dia):
            temperatura=random.randint(15, 35)
            matriz_temperaturas[i][j][k]=temperatura
            print(f"  \033[97m{dias[k]} = {matriz_temperaturas[i][j][k]} °C")
            suma_temperaturas+=matriz_temperaturas[i][j][k]
        promedio=suma_temperaturas/dia
        print(f"  \033[96mEl promedio de temperatura de la {semanas[j].lower()} en la ciudad de {ciudades[i]} es: \033[97m{promedio:.2f} °C\n")