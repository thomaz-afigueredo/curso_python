#Exercício Python 005: Faça um programa que leia um número Inteiro e mostre na tela o seu sucessor e seu antecessor.
dia=int(input('Em qual dia você deseja viajar?'))
print('Não temos viagem para o dia {}, mas temos para o dia {} ou para o dia {}'.format(dia, (dia+1),(dia-1)))
