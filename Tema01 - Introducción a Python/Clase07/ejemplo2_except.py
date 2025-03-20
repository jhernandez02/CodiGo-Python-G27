# ejemplo2_except.py

# Desarrolla un programa que muestre el contenido de demo.txt
# Cada vez que que se intente leer el contenido,
# se agregará "Hola"

try:
    with open('demo.txt') as archivo:
        contenido = archivo.read()
        print(contenido)
except:
    print('No se puede abrir el archivo')
else:
    print('Archivo leído exitosamente!')
finally:
    with open('demo.txt','a') as archivo:
        archivo.write('hola\n')
    