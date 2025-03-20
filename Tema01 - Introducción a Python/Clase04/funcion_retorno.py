#funcion_retorno.py
comision = 2
billetera = 50
def cajeroAutomatico():
    print('Inserte su tarjeta')
    monto = int(input('Ingresa el monto: '))
    return monto

dinero = cajeroAutomatico()-comision
billetera = billetera + dinero
print('billetera:',billetera)