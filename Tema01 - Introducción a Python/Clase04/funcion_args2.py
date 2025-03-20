# funcion_args2.py

def promediarNotas(nombreCurso,*args):
    total = len(args)
    suma = sum(args)
    promedio = suma/total
    print('Promedio '+nombreCurso+':',promedio)

promediarNotas('Algoritmos',12,15,18,11)
promediarNotas('Base de Datos',13,10,18)
promediarNotas('Java',13,17,10,18,9,15,17)