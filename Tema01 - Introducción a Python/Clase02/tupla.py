'''
Una tupla es una secueprint('--Acceso a los elementos--')
print(tupla1[1])ncia de objetos de Python
inmutable (no se puede modificar)
'''
tupla1 = ('Smartphone', 850, 1.2)
print(tupla1)
print(type(tupla1))

print(tupla1[2])
print(tupla1[0])
#print(tupla1[3]) # error: no existe el indice
print(tupla1[-1])
print(tupla1[-2])
print(tupla1[-3])
# print(tupla1[-7]) # error: no existe el indice

print('--Inmutable--')
#tupla1[1] = 1200 # error: no se puede modificar el valor

print('--Acceder a bloques de datos--')
tupla2 = tupla1 + ('Table', 350)
print(tupla2)
print(tupla2[0:3]) # devolvemos los elementos desde la posicion cero hasta antes de la posicion 3
print(tupla2[3:5])
print(tupla2[2:4])

print('--Definiciones complejas--')
tuplaComp = (2, 4, 'Paman Sports', (1,2),("Futbol",4,(5,8)))
print("elem1",tuplaComp[0])
print("elem2",tuplaComp[1])
print("elem3",tuplaComp[2])
print("elem4",tuplaComp[3])
print("elem5",tuplaComp[4])
print(tuplaComp[4][2][1])