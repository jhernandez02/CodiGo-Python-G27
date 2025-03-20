# Conocer si el sueldo eseta en el rango de 1025 y 2000

sueldo = 2000
# Se debe cumplir las 2 condiciones
# Caso1: no se considera 1025 ni 2000
if sueldo>1025 and sueldo<2000:
    print('C1: Tu sueldo esta en el rango de 1025 y 2000')

# Caso2: se considera 1025 y 2000
if sueldo>=1025 and sueldo<=2000:
    print('C2: Tu sueldo esta en el rango de 1025 y 2000')

sueldo = 1500
if sueldo<1025 or sueldo>2000:
    print('C3: Tu sueldo esta fuera del rango')
else:
    print('C4: Tu sueldo esta dentro del rango')

sueldo = 1024
# Si el sueldo NO es igual a 1025
if not sueldo == 1025:
    print("Tu sueldo no es el basico")


