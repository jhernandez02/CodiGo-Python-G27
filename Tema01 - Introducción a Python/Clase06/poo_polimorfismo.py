class Padre:
    nombre = 'Luis'
    edad = '45'
    def cocinar(self):
        print('Cocinando lomo saltado')
    def jugar(self):
        print('Jugando futbol')

class Hijo(Padre):
    edad = '18'
    def saludar(self):
        print ('Hola, me llamo '+self.nombre)
        print('Tengo '+self.edad+' años')
    def jugar(self):
        print('Jugando tennis')

print('--Padre:--')
padre = Padre()
padre.cocinar()
padre.jugar()

print('--Hijo:--')
hijo = Hijo()
hijo.saludar()
hijo.cocinar()
hijo.jugar()