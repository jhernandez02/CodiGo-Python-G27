productoDict = {'marca':'Akita','nombre':'pilas','precio':4}
print (productoDict)

# Actualizamos el valor
productoDict['nombre'] = 'Pilas A3'
print(productoDict)
productoDict.update({'precio':3.7})
print(productoDict)

# Añadimos un nuevo elemento:
productoDict['categoria'] = 'Herramientas'
productoDict.update({'peso':'40gr'})
print(productoDict)

# Eliminamos un elemento
productoDict.pop('peso')
print(productoDict)