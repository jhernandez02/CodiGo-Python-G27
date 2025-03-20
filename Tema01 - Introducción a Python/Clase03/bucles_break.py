# Implementar un bucles que vaya mostrando los elementos
# y se detenga en un elemento que hemos indicado para buscar
# Ej: buscar= azul => rojo, verde y azul
colores = ('rojo','verde','azul','amarillo','negro')

buscar = 'verde'

for color in colores:
    print(color)
    if color==buscar:
        print('Detenido')
        break



