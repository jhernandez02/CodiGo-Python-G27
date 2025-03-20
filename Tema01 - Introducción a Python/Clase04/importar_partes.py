# importar_partes.py
from modulo_matematicas_basicas import sumar, restar

def calculadoraBasica():
    while True:
        opcion = input('Ingresar una opcion (1,2,3,4,0): ')
        if opcion=='0':
            break
        n1 = int(input('Ingresa el primer valor: '))
        n2 = int(input('Ingresa el segundo valor: '))
        if opcion=='1':
            print('Suma:',sumar(n1,n2))
        if opcion=='2':
            print('Resta:',restar(n1,n2))

calculadoraBasica()