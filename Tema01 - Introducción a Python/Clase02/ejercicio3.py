# Desarrollar un programa que indicando el nombre de la fruta
# se elimine de la cesta
cesta = ['uva','piña','kiwi','coco','manzana']
print(cesta)
fruta = input('ingresa la fruta que deseas eliminar:')
index = cesta.index(fruta)
print('index:',index)
del(cesta[index])
print(cesta)