# ejemplo1_log.py

# Desarrolla una programa que solicite 2 números y los divida.
# El programa debe guardar los errores en el archivo error.log

from datetime import datetime

try:
    a = int(input('Número1: '))
    b = int(input('Número2: '))
    print(a/b)
except Exception as error:
    print('Ocurrió un error')
    with open('error.log','a') as archivo:
        nombreError = type(error).__name__
        descripcionError = str(error)
        fechaError = str(datetime.now())
        archivo.write('Error: '+nombreError+' | ')
        archivo.write('Description: '+descripcionError+' | ')
        archivo.write('Fecha: '+fechaError+'\n')
