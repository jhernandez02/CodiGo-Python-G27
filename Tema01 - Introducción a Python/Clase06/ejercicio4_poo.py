# ejercicio4_poo.py

# Desarrolar con POO, el software de un automovil

class Auto:
    __encendido = False
    __combustible = 30 # 0% -> 100%
    def __init__(self,marca,modelo,color,placa):
        self.__marca = marca
        self.__modelo = modelo
        self.__color = color
        self.__placa = placa

    def getEncendido(self):
        print('Encendido:',self.__encendido)

    def getCombustible(self):
        print('Combustible(%):',self.__combustible)
    
    def encender(self):
        self.__encendido = True
        print('Auto encendido!')

    def avanzar(self):
        if self.__encendido: # Verifico que el auto este encendido
            if self.__combustible>0 : # Verifico que haya combustible
                self.__combustible -= 5
                print('Auto avanzando...')
                if self.__combustible==0 : # Verifico si ya no tengo combustible
                    self.__encendido = False # Apagamos el auto
                    print('Combustible agotado!')
        else:
            print('El auto no puedo avanzar porque esta apagado')
    
    def llenarTanque(self,cantidad):
        self.__combustible += cantidad
        self.getCombustible()

auto = Auto('Tord','Toro','Azul','SOS505')
auto.getEncendido()
auto.getCombustible()
auto.avanzar()
auto.encender()
auto.avanzar()
auto.getCombustible()
auto.avanzar()
auto.avanzar()
auto.avanzar()
auto.avanzar()
auto.getCombustible()
auto.avanzar()
auto.avanzar()
auto.getCombustible()
auto.llenarTanque(80)
auto.avanzar()
auto.encender()
auto.avanzar()
auto.getCombustible()