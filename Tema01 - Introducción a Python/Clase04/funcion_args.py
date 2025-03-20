# funcion_args.py
def promediarNotas(*args):
    print(args,type(args))
    total = len(args)
    print('total:',total)
    suma = sum(args)
    print('suma:',suma)
    promedio = suma/total
    return promedio

def entregarPromedioCursoAlgoritmos():
    resultado = promediarNotas(10,14,18)
    print('Promedio Algoritmos:',resultado)

def entregarPromedioCursoBaseDatos():
    resultado = promediarNotas(10,12,17,14)
    print('Promedio Base de Datos:',resultado)

# Ejecutamos las funciones
entregarPromedioCursoAlgoritmos()
entregarPromedioCursoBaseDatos()