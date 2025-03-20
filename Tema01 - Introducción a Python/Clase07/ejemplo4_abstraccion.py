# ejemplo4_abstraccion.py

# Desarrollar un programa para generar reproductores de música

from abc import ABC, abstractmethod

class Reproductor(ABC):
    @abstractmethod
    def play(self):
        pass
    
    @abstractmethod
    def pause(self):
        pass
    
    @abstractmethod
    def stop(self):
        pass

class MP3Player(Reproductor):
    def play(self, cancion):
        print('Reproduciendo la canción '+cancion)

    def pause(self):
        print('Pausando canción')
    
    def stop(self):
        print('Deteniendo canción')
    
    def previus(self):
        print('Canción anterior')
    
    def next(self):
        print('Siguiente canción')

class MP4Player(Reproductor):
    def play(self, video):
        print('Reproduciendo el vídeo '+video)

    def pause(self):
        print('Pausando vídeo')
    
    def stop(self):
        print('Deteniendo vídeo')

mp3 = MP3Player()
mp3.play('Lucerito')

mp4 = MP4Player()
mp4.play('Sherk 3')
