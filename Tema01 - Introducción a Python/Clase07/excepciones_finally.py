# excepociones_finally.py

# El bloque "finally" se ejecutará siempre
# sin importa si hay excepciones o no

try: 
    a = int(input('Número1: '))
    b = int(input('Número2: '))
    print(a/b)
except:
    print('Ocurrió un error')
finally:
    print('Termino de ejecutarse la operación')
    # guarda la operacion en events.log