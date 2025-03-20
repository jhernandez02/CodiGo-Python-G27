# excepciones_raise.py

# raise se usa para lanzar una excepcion de forma manual
try:
    raise ValueError('Este es un error personalizado')
except Exception as error:
    print('Ocurrió un error')
    print(type(error).__name__)
    print(error)