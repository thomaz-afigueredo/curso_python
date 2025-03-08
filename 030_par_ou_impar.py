#Exercício Python 030: Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR
n=int(input('Insira um número'))
if n % 2 == 1:
    print('{} é um número ímpar'.format(n))
else:
    print('{} é um número par'.format(n))