# ejercicio2.py
# Elabore una función que lea un caracter y devuelva True si es una vocal,
# de lo contrario que de vuelva False

def verificarVocal(caracter):
    vocales = ('a','e','i','o','u')
    caracter = input('Ingresa un caracter: ')
    existe = caracter in vocales
    print(existe)

verificarVocal()