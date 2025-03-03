# Exercício Python 031: Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem,
# cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
d=float(input('Qual a distância da sua viagem?'))
small=0.50*d
l=0.45*d
if d <= 200:
    print ('O preço da sua passagem será de: R$ {:.2f}'.format(small))
else: print('O preço da sua passagem será de: R$ {:.2f}'.format(l))