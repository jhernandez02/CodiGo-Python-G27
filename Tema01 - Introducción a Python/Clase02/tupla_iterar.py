semana = ('lun','mar','mie','jue','vie','sab','dom')

for dia in semana:
    print(dia)

print('--------------')

for dia in semana:
    if dia=="lun":
        print('iniciamos la semana en lunes')
    if dia=="dom":
        print('descansamos el día domingo')