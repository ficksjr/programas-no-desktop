# Exercício Python 21: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.

import pygame
import time

pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('som.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(1)


time.sleep(20)
