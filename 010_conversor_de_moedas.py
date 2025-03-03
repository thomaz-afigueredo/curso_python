#Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
total_brl=float(input('Quantos reais (R$) você possui em carteira?'))
usd=float(5.70)
total_usd=total_brl/usd
print('Você pode converter até ${:.2f}! dólares. Aproveite!'.format(total_usd))