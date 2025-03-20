# poo_encapsulamiento.py

# El encapsulamiento restringe el acceso directo
# a ciertos atributos y métodos de una clase

class CuentaBancaria:
    def __init__(self,titular,saldo_inicial):
        self.titular = titular                  # Atributo público
        self.__saldo_inicial = saldo_inicial    # Atributo privado

    def depositar(self, monto):
        # Agregamos el monto al saldo inicial
        self.__saldo_inicial += monto
        print(f'Depósito exitoso: S/{monto}')
    
    def retirar(self, monto):
        if monto<=self.__saldo_inicial:
            # Agregamos el monto al saldo inicial
            self.__saldo_inicial -= monto
            print(f'Retiro exitoso: S/{monto}')
        else:
            print('Fondos insuficientes')

    def mostrarSaldo(self):
        # Accedemos al atributo privado __saldo_inicial
        print(f'Saldo actual: S/{self.__saldo_inicial}')

miCuenta = CuentaBancaria('Jhon',1000)
miCuenta.depositar(200)
miCuenta.retirar(700)
# No se puede acceder a un atributo privado
#print(miCuenta.__saldo_inicial)
miCuenta.mostrarSaldo()
miCuenta.retirar(700)
miCuenta.mostrarSaldo()