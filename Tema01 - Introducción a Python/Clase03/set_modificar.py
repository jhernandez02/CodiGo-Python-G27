colorSet = {'rojo','azul','verde','azul','amarillo','azul'}
print(colorSet)

# Añadir un elemento a un set
colorSet.add('blanco')
print(colorSet)

# Eliminar un elemento de un set
colorSet.remove('azul')
print(colorSet)
# No se puede modificar el valor de un elemento
#colorSet[2] = 'negro'

# Eliminar un elemento que no existe
#colorSet.remove('celeste') # Da error
existe = 'celeste' in colorSet # Consultamos si el color existe en el conjunto
if existe:
    colorSet.remove('celeste')
else:
    print('El color no existe')
print(colorSet)

# Discard elimina si encuentra el elemento, de lo contrario no hace nada, ni da error
colorSet.discard('morado')
print(colorSet)

# Eliminar todos los elementos de un set
colorSet.clear()
print(colorSet)