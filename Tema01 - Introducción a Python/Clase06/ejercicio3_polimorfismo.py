class Mascota:
    def __init__(self,nombre,color,raza):
        self.nombre = nombre
        self.color = color
        self.raza = raza
    def hacer_sonido(self):
        pass # No ejecuta nada, pero no da error

class Perro(Mascota):
    def __init__(self,nombre,color,raza):
        # Ejecutamos el constructor padre
        super().__init__(nombre,color,raza)
    def hacer_sonido(self):
        print('wow wow')

class Gato(Mascota):
    def __init__(self,nombre,color,raza):
        # Ejecutamos el constructor padre
        super().__init__(nombre,color,raza)
    def hacer_sonido(self):
        print('miau miau')

gato = Gato('Michi','Negro','Persa')
gato.hacer_sonido()

perro = Perro('Firulais','Blanco','Pitbull')
perro.hacer_sonido()