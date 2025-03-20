productoDict = {'marca':'Akita','nombre':'pilas','precio':4}

print('--Contar elementos--')
print('length:', len(productoDict))

print('--Acceso a los elementos--')
print('Marca:', productoDict['marca'])
print('Nombre:', productoDict['nombre'])
print('Precio:', productoDict.get('precio'))

print('--Acceso a las claves--')
print('Claves:',productoDict.keys())

print('--Acceso a los valores --')
print('Claves:',productoDict.values())