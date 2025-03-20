lista1 = ['auto','moto','avion']
lista2 = lista1[:]
lista3 = lista1.copy()
print('lista2:',lista2)
print('lista3:',lista3)
lista1[1] = 'helicoptero'
lista3.append('barco')
print('lista1:',lista1)
print('lista2:',lista2)
print('lista3:',lista3)
