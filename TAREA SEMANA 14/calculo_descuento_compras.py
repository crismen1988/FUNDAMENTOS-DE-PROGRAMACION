print("ELECTRO OFERTAS")
#Listas de electrodomesticos, precios y códigos
electrodomesticos=["refrigerador","cocina","microondas","lavadora","secadora"]
precios_electrodomesticos=["380.50","180.00","125.00","560.75","550.55"]
codigo_electrodomestico=["r5","c6","m7","l8","s9"]

#Funcion para generar lista de electrodomesticos, codigos y precios
def escoger_productos(electro,precio_electro,codigo_electro):
    print(f"\033[1;33m"+" Código                    Electrodoméstico               Precio                   ")
    #Utilizamos for para recorrer las listas e ir imprimiendo los nombres de los electrodomesticos con sus codigos y precios
    for i in range(len(electro)):
        print("\033[;36m"+"")
        print(f" {codigo_electro[i]}                       {electro[i]}                    {precio_electro[i]}")
  
 
#Funcion para obtener     
def venta(codigo_electro,electro,precio_producto):
    #Declaro estas variables como globales para poder utilizar en otras funciones
    print("\n\033[39m"+"")
    global total_compra
    global codigo_erroneo
    total_compra=0
    #While para pedir el codigo del producto o para salir de la venta
    while True:
        codigo_electro_usuario=input("\n\033[;39m"+"Ingrese el código del producto o 'S' para salir: ").lower()
        #Si el usuario ingresa un codigo que esta en la lista entonces pedimos el numero de artefactos a vender
        if codigo_electro_usuario in codigo_electro:
            indice_codigo=codigo_electro.index(codigo_electro_usuario)
            numero_produc=int(input("\nIngrese el número de Artefectos: "))
            precio_total=float(precio_producto[indice_codigo])*numero_produc
            print("\033[;36m"+"")
            print(f"Valor Individual: {precio_producto[indice_codigo]} $")
            print(f"Valor Total: {precio_total:.2f} $")
            total_compra+=(precio_total)
            codigo_erroneo=False
        #Si el usuario ingresa s entonces salimos de la venta
        elif codigo_electro_usuario=="s":
            break
        #Aqui verifico que el codigo es erroneo
        else:
            codigo_erroneo=True
            print("\n\033[;91m"+"***** Ingreso Un Código de Producto Erróneo *****")
       
    
#Funcion para calcular el descuento
#Existen descuentos predefinidos pero tambien hay la opcion de dar un descuento personalizado
def calcular_descuento(compra_total,descuento_personalizado=None):
    print("\n\033[39m"+"")
    #Si no hay descuento personalizado entonces se generan los predefinidos
    if descuento_personalizado is None:
        #Descuento del 0 %
        if compra_total<=200.00 and compra_total>0:
            print("\033[;36m"+"")
            print("\nLa venta tiene un descuento de 0 %")
            print(f"\nTotal a Pagar: {compra_total}")
        #Descuento del 5%
        elif compra_total>200 and compra_total<=500:
            descuento=compra_total*0.05
            print(f"\nLa venta tiene un descuento del 5 %: {descuento:.2f} $")
            total_pagar=compra_total-descuento
            print("\033[;36m"+"")
            print(f"\nTotal a Pagar con descuento: {total_pagar:.2f} $")
        #descuento del 10%
        elif compra_total>500:
            descuento=compra_total*0.1
            print(f"\nLa venta tiene un descuento del 10 %: {descuento:.2f} $")
            total_pagar=compra_total-descuento
            print("\033[;36m"+"")
            print(f"\nTotal a Pagar con descuento: {total_pagar:.2f} $")
    #Aqui se define el descuento personalizado
    else:
        descuento_personalizado=int(descuento_personalizado)
        descuento=compra_total*(descuento_personalizado/100)
        print(f"\nLa venta tiene un descuento del {descuento_personalizado} %: {descuento:.2f} $")
        total_pagar=compra_total-descuento
        print("\033[;36m"+"")
        print(f"\nTotal a Pagar con descuento del {descuento_personalizado} %: {total_pagar:.2f} $\n")

        
#Utilizamos While para generar tantas ventas como el vendedor necesite
while True:
    #Llamamos a las funciones para que nos muestren el catalogo de productos disponibles 
    escoger_productos(electrodomesticos,precios_electrodomesticos,codigo_electrodomestico)
    #Llamamos a la funcion ventas
    venta(codigo_electrodomestico,electrodomesticos,precios_electrodomesticos)
    #Llamamos a la funcion que calcula el descuento
    calcular_descuento(total_compra)
    #Si el codigo ingresado por el usuario en la funcion venta es erroneo
    if codigo_erroneo==True:
        respuesta_usuario=input("\n\033[92m"+"Presione 'N' para generar una nueva venta o Cualquier tecla para salir del sistema de ventas: ").lower()    
        if respuesta_usuario!="n":
            print("\n\033[39m"+"")
            print("\nHasta Pronto............")
            break
    #Generamos un descuento persoalizado
    elif codigo_erroneo==False:
        respuesta_descuento=input("\n\033[1;33m"+"¿Desea dar algún descuento personalizado S/N ?: ").lower()
        if respuesta_descuento=="s":
            descuento_personalizado=input("\n\033[39m"+"\nIngrese el valor del descuento personalizado: ")
            calcular_descuento(total_compra,descuento_personalizado)
        #Aqui no se da ningun descuento y terminamos la venta o generamos una nueva
        else:
            print("\n\033[39m"+"No ha dado ningún descuento\n")
            respuesta_usuario=input("\n\033[92m"+"Presione 'N' para generar una nueva venta o Cualquier tecla para salir del sistema de ventas: ").lower()    
            if respuesta_usuario!="n":
                print("\n\033[39m"+"")
                print("\nHasta Pronto............")
                break
        

        
        
        
        

   
