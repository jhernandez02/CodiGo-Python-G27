# archivo_readline.py

archivo = open('ejemplo.txt','r',encoding='utf-8')
print(archivo.readline())
print(archivo.readline())
# mostramos solo 4 caracteres
print(archivo.readline(4))
archivo.close()
