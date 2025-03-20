# archivo_lectura.py
# r = modo lectura
# encoding = grupo de caracteres que se usa
archivo = open('ejemplo.txt','r',encoding='utf-8')
print(archivo.read())
archivo.close()