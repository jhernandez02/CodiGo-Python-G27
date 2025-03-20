# ejemplo3_except_personalizado.py

# Desarrolla un programa para validar una edad
# La edad no puede ser negativa, y debe ser mayor de edad

class EdadInvalidaError(Exception):
    def __init__(self, edad, mensaje):
        self.edad = edad
        self.mensaje = mensaje
        # Enviamos el mensaje del error a la case Exception
        super().__init__(f'{mensaje}: {edad}')

try:
    edad = int(input('Edad: '))
    if edad < 0:
        raise EdadInvalidaError(edad,'La edad no puede ser negativa')
    elif edad < 18:
        raise EdadInvalidaError(edad,'Debes ser mayor de edad')
    else:
        print('Edad válida')
except Exception as err:
    print(err)
