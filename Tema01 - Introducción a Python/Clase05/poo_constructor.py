# poo_constructor.py

# El constructor es el primer método que se ejecuta de manera automática
# cuando se instancia el objeto

# poo_inicializar_datos.py

# poo_atributos.py

class Auto:
    # Atributos
    marca = ''
    modelo = ''
    anio = ''
    color = ''
    combustible = ''
    placa = ''

    def __init__(self,marca,modelo,anio,color,combustible,placa):
        # Asignamos los valores de los parámetros a los atributos de la clase
        # self indica que pertenece a la clase
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.combustible = combustible
        self.placa = placa

# Le pasamos los datos mediante el constructor de la clase
auto1 = Auto('Yotoya','Paris','1986','Verde','GLP','DON585')
print('modelo: ', auto1.modelo)
print('combustible: ', auto1.combustible)

# Le pasamos los datos mediante el constructor de la clase
auto2 = Auto('Yotoya','Eliot','2015','Rojo','Gasolina','PLA245')
print('modelo: ', auto2.modelo)
print('combustible: ', auto2.combustible)