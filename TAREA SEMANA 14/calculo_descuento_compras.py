print("ELECTRO OFERTAS")
#Listas de electrodomesticos, precios y códigos
electrodomesticos=["refrigerador","cocina","microondas","lavadora","secadora"]
precios_electrodomesticos=["380.50","180.00","125.00","560.75","550.55"]
codigo_electrodomestico=["r5","c6","m7","l8","s9"]

def escoger_productos(electro,precio_electro,codigo_electro):
    print(f"\033[1;33m"+" Código                    Electrodoméstico               Precio                   ")
    for i in range(len(electro)):
        print("\033[;36m"+"")
        print(f" {codigo_electro[i]}                       {electro[i]}                    {precio_electro[i]}")
  
     
def compra(respuesta_usuario,codigo_electro,electro,precio_producto):
    
    print("\n\033[39m"+"")
    global total_compra
    total_compra=0
    while respuesta_usuario=="s":
        codigo_electro_usuario=input("\nIngrese el código del producto: ").lower()
        if codigo_electro_usuario in codigo_electro:
            indice_codigo=codigo_electro.index(codigo_electro_usuario)
            numero_produc=int(input("\nIngrese el número de Artefectos: "))
            precio_total=float(precio_producto[indice_codigo])*numero_produc
            print("\033[;36m"+"")
            print(f"Valor Individual: {precio_producto[indice_codigo]} $")
            print(f"Valor Total: {precio_total:.2f} $")
            total_compra+=(precio_total)
        else:
            print("\nIngreso Un Código de Producto Erróneo")
        respuesta_usuario=input("\n\n\033[39m"+"Desea Agregar Otro Producto a la Compra S/N: ").lower()
    print("\033[;36m"+"")
    print(f"\nEl Total De La Venta Es: {total_compra:.2f} $")
    

def descuento(compra_total,descuento_personalizado=None):
    print("\n\033[39m"+"")
    if descuento_personalizado is None:
        if compra_total<=200.00 and compra_total>0:
            print("\033[;36m"+"")
            print("\nLa venta tiene un descuento de 0 %")
            print(f"\nTotal a Pagar: {compra_total}")
        elif compra_total>200 and compra_total<=500:
            descuento=compra_total*0.05
            print(f"\nLa venta tiene un descuento del 5 %: {descuento:.2f} $")
            total_pagar=compra_total-descuento
            print("\033[;36m"+"")
            print(f"\nTotal a Pagar con descuento: {total_pagar:.2f} $")
        else:
            descuento=compra_total*0.1
            print(f"\nLa venta tiene un descuento del 10 %: {descuento:.2f} $")
            total_pagar=compra_total-descuento
            print("\033[;36m"+"")
            print(f"\nTotal a Pagar con descuento: {total_pagar:.2f} $")
    else:
        descuento_personalizado=int(descuento_personalizado)
        descuento=compra_total*(descuento_personalizado/100)
        print(f"\nLa venta tiene un descuento del {descuento_personalizado} %: {descuento:.2f} $")
        total_pagar=compra_total-descuento
        print("\033[;36m"+"")
        print(f"\nTotal a Pagar con descuento del {descuento_personalizado} %: {total_pagar:.2f} $")

        
respuesta_usuario="s"
while respuesta_usuario=="s":
    escoger_productos(electrodomesticos,precios_electrodomesticos,codigo_electrodomestico)
    compra(respuesta_usuario,codigo_electrodomestico,electrodomesticos,precios_electrodomesticos)
    descuento(total_compra)
    respuesta_descuento=input("\n\033[1;33m"+"¿Desea dar algún descuento personalizado S/N ?: ").lower()
    if respuesta_descuento=="s":
        descuento_personalizado=input("\n\033[39m"+"\nIngrese el valor del descuento personalizado: ")
        descuento(total_compra,descuento_personalizado)
    else:
        print("\n\033[39m"+"\nNo ha dado ningún descuento")
    print("\n\033[39m"+"")
    respuesta_usuario=input("\nPresione 'S' para generar una nueva venta o Cualquier tecla para salir del sistema de ventas: ")    
print("\nHasta Pronto..........")

        
        
        
        

   
