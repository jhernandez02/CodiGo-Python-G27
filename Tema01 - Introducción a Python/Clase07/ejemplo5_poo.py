# ejemplo5_poo.py

# Desarrolla la logica de un reproductor de música
# Funciones:
# 1. Cargar una lista de canciones
# 2. Seleccionar una canción para reproducirla
# 3. Mostrar la canción que se esta reproduciendo
# 4. Pausar la canción
# 5. Detener la reproducción de una canción

class MP3Player:
    lista = []
    cancion_actual = ''
    indice_actual = 0

    def cargarLista(self, lista):
        self.lista = lista

    def play(self):
         # Verifico si la lista tiene canciones
        if len(self.lista) > 0 :
            # Verifico si se ha selecciona una canción
            if self.cancion_actual=='':
                print('Reproduciendo '+self.lista[0])
            else:
                self.indice_actual = self.lista.index(self.cancion_actual)
                print('Reproduciendo '+self.cancion_actual)
        else:
            print('La lista de canciones esta vacía')
    
    def seleccionarCancion(self, cancion):
        self.cancion_actual = cancion
        self.play()

    def siguienteCancion(self):
        print('Siguiente canción')
        indice_siguiente  = self.indice_actual + 1
        try:
            self.seleccionarCancion(self.lista[indice_siguiente])
        except IndexError:
            print('No hay más canciones en la lista')
    
    def previaCancion(self):
        print('Anterior canción')
        indice_anterior  = self.indice_actual - 1
        self.seleccionarCancion(self.lista[indice_anterior])


mp3 = MP3Player()
mp3.play()
mp3.cargarLista(['Baladitas','Himno','Cumpleaños','Navidad','Toneras'])
mp3.play()
mp3.seleccionarCancion('Navidad')
mp3.siguienteCancion()
mp3.siguienteCancion()
mp3.seleccionarCancion('Himno')
mp3.previaCancion()
mp3.previaCancion()
mp3.previaCancion()
