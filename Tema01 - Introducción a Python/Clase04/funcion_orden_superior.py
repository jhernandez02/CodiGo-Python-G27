#funcion_orden_superior.py

def duplicar(numero):
    return numero*2

def cuadrado(numero):
    return numero**2

def ejecutarFuncion(funcion,numero):
    resultado = funcion(numero)
    print(resultado)

ejecutarFuncion(cuadrado,5) # Output: 25
ejecutarFuncion(duplicar,7) # Output: 14