# archivo_writelines.py

# \n => genera un salto de línea
lista = ['Azul\n','Rojo\n','Verde']
archivo = open('colores.txt','w',encoding='utf-8')
archivo.writelines(lista)
archivo.close()