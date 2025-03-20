# ejercicio2_poo.py

# Desarrolla una programa con POO, que te solicite un número
# y te devuelva el valor al cuadrado y al cubo
# Ej:
# Input: 6
# Output: Cuadrado: 36
# Output: Cubo: 216

class Numero:
    valor=0
    def __init__(self,numero):
        self.valor = numero

    def cuadrado(self):
        return self.valor**2
    
    def cubo(self):
        return self.valor**3
num = int(input('Ingrese número: '))
numero = Numero(num)
print('Cuadrado:',numero.cuadrado())
print('Cubo:',numero.cubo())