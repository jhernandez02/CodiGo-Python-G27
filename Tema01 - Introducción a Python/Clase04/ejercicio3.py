# ejercicio3.py

# Escribir una función que calcule el total de una boleta de venta
# aplicandole el IGV (18%). La funcion debe recibir la cantidad de la
# venta. Si el monto total de la venta supera los 500 soles, se aplica
# un descuento del 10%.

def calcularPrecioVenta(monto):
    if monto>500:
        cobrar = monto*0.9
        print('Precio con Descuento:',round(cobrar,2))
        precioVenta = cobrar*1.18
    else:
        print('Precio:',monto)
        precioVenta = monto*1.18
    return round(precioVenta,2)

precio = int(input('Ingrese el monto de su compra:'))
print('Precio final con IGV:',calcularPrecioVenta(precio))