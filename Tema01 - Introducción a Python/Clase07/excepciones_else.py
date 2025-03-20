# excepciones_else.py

# El código del bloque "else", se ejecutará si no ha ocurrido ninguna excepción
try: 
    a = int(input('Número1: '))
    b = int(input('Número2: '))
    print(a/b)
except:
    print('Ocurrió un error')
    # guardo el error en error.log
else:
    print('Operación sin errores')
    # guardo la operacion en events.log
