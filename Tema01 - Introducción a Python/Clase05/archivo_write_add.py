# archivo_write_add.py

# a =>  añade contenido a un archivo,
#       si el archivo no existe, lo crea
archivo = open('frutas.txt','a',encoding='utf-8')
archivo.write('Manzana\n')
archivo.write('Durazno\n')
archivo.close()