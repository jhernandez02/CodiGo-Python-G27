# excepciones_personalizadas.py

# Una excepción personaliza es útil para manejar errores específicos de tu programa
# Puedes crear excepciones personalizadas definiendo una clase que herede de Exception

class MiError(Exception):
    def __init__(self, mensaje):
        self.mensaje = mensaje
        # Envio el mensaje al constructor de la clase Exception
        super().__init__(self.mensaje)

try:
    # Lanzamos la excepción MiError manualmente
    raise MiError('Ocurrió un error personalizado')
except Exception as err:
    print(type(err).__name__)
    print(err)

try:
    # Lanzamos la excepción MiError manualmente
    raise MiError('Ocurrió un error personalizado')
except MiError as err:
    print(err)