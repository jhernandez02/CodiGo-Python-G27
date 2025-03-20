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

    def inicializar(self,marca,modelo,anio,color,combustible,placa):
        # Asignamos los valores de los parámetros a los atributos de la clase
        # self indica que pertenece a la clase
        self.marca = marca
        self.modelo = modelo
        self.anio = anio
        self.color = color
        self.combustible = combustible
        self.placa = placa

# Instanciamos de la clase Auto
auto1 = Auto()
auto1.inicializar('Yotoya','Paris','1986','Verde','GLP','DON585')
print('marca: ', auto1.marca)
print('placa: ', auto1.placa)