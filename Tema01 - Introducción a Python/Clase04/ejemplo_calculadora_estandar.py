from modulo_matematicas_basicas import *
from modulo_matematicas_calculos import potencia, sumar as sumaAvanzada

def calculadoraEstandar():
    while True:
        opcion = input('Ingresar una opcion (1,2,3,4,5,6,0): ')
        if opcion=='0':
            break
        n1 = int(input('Ingresa el primer valor: '))
        n2 = int(input('Ingresa el segundo valor: '))
        if opcion=='1':
            print('Suma:',sumar(n1,n2))
        if opcion=='2':
            print('Resta:',restar(n1,n2))
        if opcion=='5':
            print('Potencia:',potencia(n1,n2))
        if opcion=='6':
            print('Suma Avanzada:',sumaAvanzada(n1,n2))

calculadoraEstandar() 