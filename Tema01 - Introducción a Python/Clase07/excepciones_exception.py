# excepciones_exception.py

try:
    a = int(input('Número1: '))
    b = int(input('Número2: '))
    print(a/b)
except Exception as error:
    print('Ha ocurrido un error:')
    print('Nombre Error: ', type(error).__name__)
    print('Descripción Error: ',error)