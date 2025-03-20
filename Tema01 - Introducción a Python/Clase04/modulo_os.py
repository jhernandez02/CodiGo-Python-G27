# modulo_os.py

import os

# Obtener la ruta del directorio actual
directorio_actual = os.getcwd()
print('directorio_actual:',directorio_actual)

# Obtener el contenido de la carpeta actual
contenido_actual = os.listdir()
print(contenido_actual)

nombre_directorio = 'demo'
nombre_nuevo = 'demo_new'

#Validar la ruta de una carpeta o archivo
if os.path.isdir(nombre_nuevo):
    # Eliminar una carpeta
    os.rmdir(nombre_nuevo)
    print('la carpeta fue eliminada')
     #Crea un directorio
    os.mkdir(nombre_directorio)
    print('carpeta creada')
    # Renombrar una carpeta o archivo
    os.rename(nombre_directorio, nombre_nuevo)
    print('carpeta renombrada')
else:
     #Crea un directorio
    os.mkdir(nombre_nuevo)
    print('nueva carpeta creada')
    
