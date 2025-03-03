#Exercício Python 018: Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
from math import cos, sin, tan, radians

a=float(input('Qual o ângulo?'))
seno=sin(radians(a))
cosseno=cos(radians(a))
tangente=tan(radians(a))
print('Do ângulo {:.0f}º temos o seno: {:.2f}, cosseno {:.2f} e tangente {:.2f}.'.format(a,seno,cosseno,tangente))