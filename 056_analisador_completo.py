# Exercício Python 056: Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
mais_velho = 0
cmulheres = 0
media = 0
nome_mais_velho = ''
for p in range (1,5):
    print('-' * 5 , '{}ª PESSOA'.format(p) , '-' * 5)
    nome = input('Qual seu nome? ').strip()
    idade = int(input('Qual sua idade? '))
    sexo = input('Sexo [M/F]: ').strip().lower()
    soma_idade += idade
    media = soma_idade / p
    if p == 1 and sexo == 'm':
        mais_velho = idade
        nome_mais_velho = nome
    if idade > mais_velho and sexo == 'm':
            mais_velho = idade
            nome_mais_velho = nome
    if sexo == 'f' and idade < 20:
        cmulheres += 1
print('{} é o homem mais velho com {} anos.\n'
      'A média de idade do grupo é de {:2} anos\n'
      'E existem {} mulheres com menos de 20 anos'.format(nome_mais_velho, mais_velho , media , cmulheres))