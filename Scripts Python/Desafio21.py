#Faça  um programa que abra e reproduza o áudio de um arquivo MP3.

import pygame
pygame.mixer.init()
pygame.mixer.music.load('withoutme.mp3')
pygame.mixer.music.set_volume(0.2)
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)



"""As linhas de commando aparentemente mudaram desde o video da aula para os de hoje em dia
Principalmente na parte final do código 
tendo que utilizar o "While (enquanto)"
praticamente falando pro programa esperar enquando a musica reproduz e verifique a cada 10ms 

Adicionado uma linda de volume, porque eu estava ficando surdo
Utilizando o Set_volume pra receber um numero float entre 0.0 a 1.0 pra representar de 0 a 100%,  sendo 0,5 = 50%"""

#Exercício Correto