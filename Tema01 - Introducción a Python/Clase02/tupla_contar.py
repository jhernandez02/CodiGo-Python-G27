notas = (9,11,16,18,20,13,10,15,16,9,19,13,9,13)
total = len(notas)
print('Total de elementos:',total)
print('Cantidad de 13s:', notas.count(13))

# Hallamos cuantas veces se repite la minima nota
minima_nota = min(notas)
print('minima nota:',minima_nota)
print('cuantos tienen la minima nota:',notas.count(minima_nota))