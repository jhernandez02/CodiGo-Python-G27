# ejercicio2_archivo.py

# Desarrolla un programa que añada por linea
# el nombre, telefono y email de un contacto
# separado por ";" (punto y coma)
# Ej:
# Juan Perez;98765431;jperez@mail.com
# Silvia Mendoza;999888444,smendoza@mail.com

nombre = input('Tu nombre: ')
telefono = input('Tu teléfono: ')
email = input('Tu email: ')

with open('agenda.txt','a',encoding='utf-8') as archivo:
    archivo.write(nombre+';')
    archivo.write(telefono+';')
    archivo.write(email+'\n')