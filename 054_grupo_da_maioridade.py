# Exercício Python 054: Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
atual = date.today().year
cmaior = 0
cmenor = 0
for pess in range (1,8):
    nasc = int(input('Qual a data de nascimento da {}ª pessoa? '.format(pess)))
    idade = atual - nasc
    if idade >= 18:
        cmaior += 1
        print('Esta pessoa é MAIOR')
    if idade < 18:
        cmenor += 1
        print('Esta pessoa é MENOR')
print('Ao todo tivemos {} pessoas maiores de idade\n'
      'E também tivemos {} pessoas menores de idade'.format(cmaior , cmenor))