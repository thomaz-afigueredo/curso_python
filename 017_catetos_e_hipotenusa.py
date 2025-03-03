#Exercício Python 017: Faça um programa que leia o
# comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.
from math import hypot
co=float(input('Insira o cumprimento do cateto oposto'))
ca=float(input('Insira o cumprimento do cateto adjacente'))
hip=hypot(ca,co)
print('O comprimento da hipotenusa é {:.2f}'.format(hip))