#Tocador de MP3
import pygame
pygame.mixer.init()
#A seguir adicionamos a música, se ela estiver na mesma pasta, só colocar nome e formato
#caso não tiver na mesma pasta, adicionar caminho do diretório até a música.
pygame.mixer.music.load('sanholo.mp3')
pygame.mixer.music.play()
#Na nova versao do python tem que adicionar input() para reprodução.
input()
pygame.event.wait()
