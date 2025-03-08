# 45: Crie um programa que faça o computador jogar jokenpô com você.
from time import sleep
from random import randint
itens=('PEDRA','PAPEL','TESOURA')
print('''Suas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA''')
player=int(input('Qual é a sua jogada? '))
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
sleep(1)
pc=randint(0,2)
print('-=-'*8)
print('Computador jogou {}'.format(itens[pc]))
print('Jogador jogou {}'.format(itens[player]))
print('-=-'*8)
if pc == 0:
    if player == 0:
        print('EMPATOU')
    elif player == 1:
        print('JOGADOR VENCE')
    elif player == 2:
        print('COMPUTADOR VENCE')
    else:
        print('OPÇÃO INVÁLIDA')
elif pc == 1:
    if player == 0:
        print('COMPUTADOR VENCE')
    elif player == 1:
        print('EMPATOU')
    elif player == 2:
        print('JOGADOR VENCEU')
    else:
        print('OPÇÃO INVÁLIDA')
elif pc == 2:
    if player == 0:
        print('JOGADOR VENCEU')
    elif player == 1:
        print('COMPUTADOR VENCEU')
    elif player == 2:
        print('EMPATOU')
    else:
        print('OPÇÃO INVÁLIDA')