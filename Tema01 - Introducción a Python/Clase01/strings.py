mensaje = 'Mi nuevo mensaje'
print(mensaje)

print('Primer caracter:',mensaje[0])
print('Último caracter:',mensaje[15])

nuevo_mensaje = "Python es muy bacan"
print(nuevo_mensaje)
print('Primer caracter:',nuevo_mensaje[0])
size = len(nuevo_mensaje)
print('Cantidad de caracteres:',size)
print('Último caracter:',nuevo_mensaje[size-1])

mensaje = 'Python es chevere'
print(mensaje)
print('Cantidad de caracteres:',len(mensaje))
# [start_index:stop_index:step]
print('mensaje[3:13:2]:',mensaje[3:13:2])
print('mensaje[-3:-11:-3]:',mensaje[-3:-11:-3])

texto = 'Mi nuevo Mensaje'
print(texto)
print(texto.upper()) # convierte a mayúsculas
print(texto.lower()) # convierte a minúsculas
print(texto.swapcase()) # convierte mayusculas a minusculas y minusculas a mayusculas
print(texto.capitalize()) # convierte todo a minusculas y a mayuscula solo la primera letra
