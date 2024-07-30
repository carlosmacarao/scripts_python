import pygame

def toca_musica():
    pygame.init()
    pygame.mixer.music.load('ex021.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()

toca_musica()    
