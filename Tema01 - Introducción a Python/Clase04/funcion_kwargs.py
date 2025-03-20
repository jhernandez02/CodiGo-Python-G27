# funcion_kwargs.py

def mostraDatosMascota(**kwargs):
    print(kwargs,type(kwargs))
    for k, v in kwargs.items():
        print(k,v)

mostraDatosMascota(nombre='Firulais',tipo='conejo')
mostraDatosMascota(nombre='Chuletas',tipo='cerdo',color='pinky')