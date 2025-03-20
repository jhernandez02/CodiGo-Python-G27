# Solicitar los datos correspondientes
# para hallar la hipotenusa
cat1 = input('Ingrese el primer cateto: ')
cat2 = input('Ingrese el segundo cateto: ')
a = int(cat1) # convertimos el valor a entero
b = int(cat2) # convertimos el valor a entero
hipotenusa = (a**2 + b**2)**0.5
print('La hipotenusa es: ',hipotenusa)