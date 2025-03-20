# poo_herencia.py

class FiguraGeometrica():
    def __init__(self,nombre,lados):
        self.nombre = nombre
        self.lados = lados
    def getInfo(self):
        print('El '+self.nombre+' tiene '+self.lados+' lados')

# Cuadrado hereda los atributos y métodos de la clase FiguraGeometrica
class Cuadrado(FiguraGeometrica):
    def __init__(self,lado):
        self.lado = lado
        # Accedemos a la clase padre (FiguraGeometrica)
        super().__init__('cuadrado','4')
    def area(self):
        return self.lado**2

class Triangulo(FiguraGeometrica):
    def __init__(self,base, altura):
        self.base = base
        self.altura = altura
        super().__init__('triángulo','3')
    def area(self):
        return (self.base*self.altura)/2


f1 = Cuadrado(7) # Inicializamos el valor del lado
f1.getInfo()
print('Area del '+f1.nombre+': ',f1.area())

f2 = Triangulo(10,7) # Inicializamos la base y la altura
f2.getInfo()
print('Area del '+f2.nombre+': ',f2.area())
