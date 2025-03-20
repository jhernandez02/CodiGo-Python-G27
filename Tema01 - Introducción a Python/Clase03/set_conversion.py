colorList = ['rojo','azul','verde','rojo','azul','amarillo','azul','rojo']
# Obtenen los colores únicos
coloresUnicos = []
for color in colorList:
    existe = color in coloresUnicos
    if existe==False:
        coloresUnicos.append(color)
print(coloresUnicos)
# Convierto la lista a un conjunto
colorSet = set(colorList)
print(colorSet)
