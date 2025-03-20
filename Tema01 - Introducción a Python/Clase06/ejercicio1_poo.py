#ejercicio1_poo.py

# Desarrolla una aplicacion en POO, que halle el perimetro y area 
# de un cuadrado brindado solo el lado.
class Cuadrado:
    # Atributos
    lado = 0 # lado = 5
    # Constructor
    def __init__(self,lado):
        self.lado = lado
    # Métodos
    def area(self):
        return self.lado**2

    def perimetro(self):
        return self.lado*4

valor = int(input('Ingresa el valor del lado del cuadrado: '))
# Inicializando el valor de lado por medio del constructor de la clase
c1 = Cuadrado(valor)
print('Area:',c1.area())
print('Perímetro:',c1.perimetro())
