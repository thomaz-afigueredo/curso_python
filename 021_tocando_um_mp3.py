#Exercício Python 021: Faça um programa em Python que abra e reproduza o áudio de um arquivo MP3.
import pygame
pygame.init()
pygame.mixer_music.load('musica.mp3')
pygame.mixer_music.play()
input()

