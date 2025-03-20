# Desarrolla un programa que solicite:
# - Tu color favorito
# - Tu comida favorita
# - Tu pasatiempo favorito
# y guardamo el archivo como favoritos.txt

color = input('Tu color favorito: ')
comida = input('Tu comida favorita: ')
pasatiempo = input('Tu pasatiempo favorito: ')

with open('favoritos.txt','w',encoding='utf-8') as archivo:
    archivo.write('color: '+color+'\n')
    archivo.write('comida: '+comida+'\n')
    archivo.write('pasatiempo: '+pasatiempo)
