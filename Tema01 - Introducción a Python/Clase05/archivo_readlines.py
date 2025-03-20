# archivo_readlines.py

archivo = open('ejemplo.txt','r',encoding='utf-8')
lineas = archivo.readlines()
print(lineas)
for linea in lineas:
    print(linea)
archivo.close()