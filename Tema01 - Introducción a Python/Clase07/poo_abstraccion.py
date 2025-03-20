# poo_abstraccion.py

# Una clase abstracta no se puede instanciar
# Una clase abstracta define los métodos que deben ser implementadas en las clases hijas
# Se debe importar ABC y abstractmethod del módulo abc (Abstract Base Clases)

from abc import ABC, abstractmethod 

class Mascota(ABC):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Mascota):
    def hacer_sonido(self):
        print('wow wowo')

class Gato(Mascota):
    def hacer_sonido(self):
        print('miau miau')

# No se puede instanciar la clase Mascota por ser abstracta
#mascota = Mascota()

perro = Perro()
perro.hacer_sonido()

gato = Gato()
gato.hacer_sonido()

