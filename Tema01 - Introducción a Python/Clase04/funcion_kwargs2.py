# funcion_kwargs2.py

def mostrarDatosMascota(nombre,tipo,**kwargs):
    print('nombre:',nombre)
    print('tipo:',tipo)
    for k,v in kwargs.items():
        print(k,':',v)

mostrarDatosMascota('Chuletas','cerdo',color='pinky',edad=3,raza='Pig')