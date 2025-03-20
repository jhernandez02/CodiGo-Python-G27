# funcion_retorno2.py

# Crear una aplicación que solicite el lado de un cuadrado
# y retorno el area y perimetro del cuadrado

def area_perimetro_cuadrado(lado):
    area = lado**2
    perimetro = lado*4
    # Retornamos 2 variables
    return area, perimetro

val_area, val_perimetro  = area_perimetro_cuadrado(6)
print('val_area:',val_area)
print('val_perimetro:',val_perimetro)
