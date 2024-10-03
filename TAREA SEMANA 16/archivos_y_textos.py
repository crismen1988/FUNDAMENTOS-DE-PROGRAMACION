#Escritura del Archivo
with open('my_notes.txt', 'w') as archivo:
    # Escribimos líneas de notas en el archivo.
    archivo.write("La inteligencia artificial mejora la eficiencia,\n")
    archivo.write("automatiza tareas complejas, impulsa la innovación\n")
    archivo.write("y facilita la toma de decisiones basadas en datos \n")
    archivo.write("en diversos sectores.\n")

# Lectura de Archivo de Texto

# Abrimos el archivo en modo de lectura ('r') para leer su contenido.
with open('my_notes.txt', 'r') as archivo:
    # Leemos y mostramos el contenido línea por línea utilizando un bucle.
    linea = archivo.readline()  # Lee la primera línea
    while linea:
        print(linea.strip())  # Imprime la línea sin el salto de línea final
        linea = archivo.readline()  # Lee la siguiente línea

# El archivo se cierra automáticamente al salir del bloque utilizando 'with'.