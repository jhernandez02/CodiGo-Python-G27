# modulo_random.py

import random

# Numero aleatorio entre 0 y 1
numero_aletario = random.random()
print('numero_aletario:',numero_aletario)

# Numero aleatorio entre un rango
rango_inicial = 5
rango_final = 15
numero_aletario_uno = random.uniform(rango_inicial,rango_final)
numero_aletario_dos = random.uniform(rango_inicial,rango_final)
print('numero_aletario_uno:',numero_aletario_uno)
print('numero_aletario_dos:',numero_aletario_dos)