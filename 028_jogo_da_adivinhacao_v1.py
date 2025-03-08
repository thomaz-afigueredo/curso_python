#Exercício Python 028: Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
#e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
#O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep
print('-=-'*27)
print('Consegue adivinhar o número em que estou pensanado? Podemos fazer uma aposta')
print('-=-'*27)
num_pc=randint(0,5)
print('Estou pensando em um número de 0 a 5...')
sleep(5)
num_usuario=int(input('Tente adivinhar, insira um número:'))
if num_pc==num_usuario:
    print('Acertou, parabéns! Você inseriu o número {} e eu pensei exatamente no número {}!'.format(num_usuario,num_pc))
else:
    print('Errou, você inseriu {}, mas eu pensei no número {}'.format(num_usuario,num_pc))

