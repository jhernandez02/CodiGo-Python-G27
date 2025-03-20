print('--Busqueda de elementos--')
colores = ('rojo','azul','verde','negro','verde')
print(colores.index('verde')) # Output: 2
print(colores.index('rojo')) # Output: 0
#print(color.index('celeste')) # Output: Error elemento o definido

print('--Consulta de elementos--')
existe_color1 = "celeste" in colores
existe_color2 = "verde" in colores
print('Consulta del color celeste:',existe_color1)
print('Consulta del color verde:',existe_color2)