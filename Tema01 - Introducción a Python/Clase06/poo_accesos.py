# poo_accesos.py

# Tipo de accesos atributos/métodos:
# - Público (public): Se pueden acceder desde cualquier parte
# - Protegido (protected): Se pueden acceder dentro de la clase y subclases
#   Convención: _nombre
# - Privado (private): Solo pueden acceder dentro de la clase
#   Convención: __nombre

class Padre:
    nombre='Juan'   # Atributo publico
    _edad=58        # Atributo protegido
    __dni = '01234567' # Atributo privado

    def getDni(self):
        # Accedemos al atributo privado
        print('DNI:',self.__dni)

class Hijo(Padre):
    nombre = 'Luis'
    def getDatosPadre(self):
        print('--Datos del padre--')
        print('Nombre: ',super().nombre)
        print('Edad: ',super()._edad)
        # No se puede heredar un atributo privado
        #print('DNI: ',super().__dni) # Output: Error

padre = Padre()
print('Nombre:',padre.nombre)
print('Edad:',padre._edad) # Funciona pero No es buena practica
# No se puede acceder un atributo privado desde el objeto
#print('DNI:',padre.__dni) # Output: Error
padre.getDni()

hijo = Hijo()
hijo.getDatosPadre()