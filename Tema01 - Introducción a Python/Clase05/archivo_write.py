# archivo_write.py

# w => reemplaza el contenido del archivo
archivo = open('datos.txt','w',encoding='utf-8')
archivo.write('Contenido línea 1\n')
archivo.write('Contenido línea 2\n')
archivo.write('Contenido línea 3')
archivo.close()
