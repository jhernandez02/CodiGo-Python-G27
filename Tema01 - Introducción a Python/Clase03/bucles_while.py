condicion = True
cont = 0
while condicion:
    numero = int(input('Ingresa un numero:'))
    cont = cont+1 # Incremento el contador en 1
    if numero<10:
        condicion = False

print(cont)

print('-------------------')
pacientes  = ('Silvia','Carlos','Miguel','Karen','Luis','Ana')
atendidos = 0 # 1,2,3,4,5,6
totalPacientes = len(pacientes)
print('totalPacientes:',totalPacientes)

while atendidos<totalPacientes:
    print('Atendiendo a ', pacientes[atendidos])
    atendidos = atendidos + 1

print('He antendido a ',atendidos, 'pacientes')