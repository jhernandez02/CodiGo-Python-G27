# ejercicio3_archivo.py

# Desarrolla un programa que pregunte por tu nombre 
# y luego te pida adivinar un numero entre el 7 y 11
# El resultado debe almacenarse en el archivo juegos.txt
# Ej: Nombre,intentos
# Ramon,2
# Silvia,3
# Pedro,5

import random

rango_inicial = 7
rango_final = 11
aleatorio = round(random.uniform(rango_inicial,rango_final))
print('aleatorio:',aleatorio)

intentos = 0
nombre = input('Tu nombre: ')

while True:
    intentos +=1
    numero = int(input('Adivina un número entre 7 y 11: '))
    if numero==aleatorio:
        print('Adivinaste el número!')
        archivo = open('juegos.txt','a',encoding='utf-8')
        # con str convierto a texto el numero de intentos
        archivo.write(nombre+','+str(intentos)+'\n')
        archivo.close()
        break