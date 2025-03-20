# Progración Orientada a Objetos (POO)
# Pilares de la POO:
# - Herencia
# - Abstracción
# - Polimorfismo
# - Encapsulamiento

# Auto: color, marca, modelo, combustible
#       arrancar, frenar, doblar,
# Personas: nombre, genero, nacionalidad, profesion
#       hablar, cantar, pintar, programar

# Class: Una clase es una plantilla, donde se define las características y funcionalidad de un objeto
# Objetos: Tienes atributos (características) y métodos (funcionalidades)
# Instanciar: la creacion de un objecto basado en una clase

class Perro:
    # Atributos
    nombre = 'Firulais'
    raza = 'Pekines'
    color = 'Marrón oscuro medio teñido claro zanahoria'
    fecha_nac = 'NS'
    # Métodos
    def ladrar(self):
        print('wou wou wou')
    
    def saltar(self):
        print('perrito saltando...')
    
    def comer(self):
        print('perrito comiendo su ricocan')
    
# Instanciamos un objeto de la clase Perro
mi_perro = Perro()
# Accedemos al método de la clase
mi_perro.ladrar()
# Modificamos el atributos de la clase
mi_perro.nombre = 'Chanclas'
# Accedemos al atributo de la clase
print('mi_perro:',mi_perro.nombre)

mi_perro2 = Perro()
mi_perro2.comer()
mi_perro2.nombre = 'Pitucho'
print('mi_perro2:',mi_perro2.nombre)