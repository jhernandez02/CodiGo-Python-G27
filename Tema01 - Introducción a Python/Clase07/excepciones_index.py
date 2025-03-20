lista = ['uva','pera','fresa']

try:
    print(lista[0])
    print(lista[5])
except IndexError:
    print('Índice inválido')