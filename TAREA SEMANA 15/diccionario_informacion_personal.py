#Funcion para generar un diccionario con datos preestableciidos
def informacion():
    print("\033[33m"+"INFORMACION PERSONAL")
    #declaramos el diccionario como global para poder reutilzar en otras funciones
    global informacion_personal
    #Definimos claves y valores del diccionario
    informacion_personal={"nombre":"cristopher","apellido":"mancero","edad":"36","ciudad":"cuenca"}
    #Iteramos en el diccionario para imprimir sus claves y valores, utilizamos la funcion items
    for clave,valor in informacion_personal.items():
        print("\033[36m"+"")
        print(f"{clave.capitalize()}: "+"\033[39m"+""+f"{valor.capitalize()}\n")
#Llamamos a la función      
informacion()

#Definimos otra funcion para cambiar la ciudad
def cambio_ciudad():
    print("\033[92m"+"MODIFICAR CLAVE CIUDAD\n")
    #Se pide ingresar la nueva ciudad
    nueva_ciudad=input("\033[39m"+"Ingrese el nombre de la ciudad: ")
    #Ingresamos el nuevo valor a la clave ciudad
    informacion_personal["ciudad"]=nueva_ciudad
    print("Se Agrego la ciudad correctamente")
#Llamamos a la funcioin
cambio_ciudad()

#Definimos una funcion para agregar y eliminar claves
def agregar_eliminar_claves():
    informacion_personal["profesión"]="electricista"
    print("\n\033[92m"+"VERIFICAMOS SI EXIsTE LA CLAVE TELEFONO EN EL DICCIONARIO")
    #claves se utilza para saber que claves existen en el diccionario
    claves=informacion_personal.keys()
    #clave se le dio el nombre de telefono
    clave="teléfono"
    print("\033[39m"+"")
    #verificamos si la clave existe dentro de las claves obtenidas
    if clave in claves:
        #Si existe la clave
        print("Si existe esa clave")     
    else:
        #No existe la clave
        print("No existe esa clave\n") 
        print("AGREGAMOS LA CLAVE TELEFONO AL DICCIONARIO\n") 
        #Agregamos la clave telefono y su valor
        informacion_personal["teléfono"]="021542122"
    #Eliminamos la clave edad
    print("\033[33m"+"ELIMINAMOS LA CLAVE EDAD\n")
    del(informacion_personal["edad"])
    #Imprimimos el diccionario final 
    print("\033[92m"+"DICCIONARIO FINAL")
    for clave,valor in informacion_personal.items():
        print("\033[36m"+"")
        print(f"{clave.capitalize()}: "+"\033[39m"+""+f"{valor.capitalize()}\n")
        
agregar_eliminar_claves()