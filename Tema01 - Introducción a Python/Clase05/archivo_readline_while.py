# archivo_readline_while.py

# with cierra automaticamente el archivo
with open('ejemplo.txt','r',encoding='utf-8') as archivo:
    linea = archivo.readline()
    # mientra la linea no esta vacia
    while linea !='':
        print(linea)
        # Obtengo el contenido de la siguiente linea
        linea = archivo.readline()
