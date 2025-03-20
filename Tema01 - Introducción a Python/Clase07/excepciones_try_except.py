# excepciones_try_except.py

# Manejamos los errores que puedan ocurrir
# dentro del bloque try
try:
    a = input('Numero: ')
    print(a**2)
except TypeError:
    print('Tipo de dato inválido')

try:
    a = int(input('Número 1: '))
    b = int(input('Número 2: '))
    print('División: ', a/b)
except ZeroDivisionError:
    print('No se puede dividir entre cero')
except ValueError:
    print('Valores inválidos')
