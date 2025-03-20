# poo_metodos.py

class Mascota:
    # Atributos
    nombre = ''
    especie = ''

    def __init__(self,nombre,especie):
        self.nombre = nombre
        self.especie = especie

    def getNombre(self):
        # Muestro el valor del atributo nombre
        print('nombre: ',self.nombre)
    
    def getEspecie(self):
        # Muestro el valor del atributo especie
        print('especie: ',self.especie)

# Un objeto es resultado concreto de instanciar una clase
# Una instancia es el acto de crear un objeto a partir de una clase
# Se inicializa una instancia

mascota1 =  Mascota('Firulais','vaca')
mascota1.getNombre()
mascota1.getEspecie()