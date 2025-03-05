# 36: Escreva um programa para aprovar um emprestimo bancário para a compra de uma casa.
# O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

casa=float(input('Qual o valor da casa?'))
salario=float(input('Qual é o seu salário?'))
anos=int(input('Em quanto anos pagará o empréstimo?'))

#meses=anos*12
mensal=casa/(anos*12)
#porcent=salario*30/100
#regra1=mensal<=salario*30/100 #valor mensal não pode ser maior que 30% do salario

if mensal <= salario*30/100:
    print ('Parabéns! Seu empréstimo foi aprovado!\n'
           'O valor do seu imóvel é de R$ {:.2f}, você pretende financiá-lo em {} vezes de R$ {:.2f}\n'
           'O valor mensal de R$ {:.2f} não excederá 30% da sua renda (renda R$ {:.2f}, 30% de R$ {:.2f})!'.format(casa,anos*12,casa/(anos*12),casa/(anos*12),salario,salario*30/100))
else: print('Seu empréstimo não foi aprovado!\n'
            'O valor mensal de (R$ {:.2f}) excederá 30% da sua renda (renda R$ {:.2f}, 30% de R$ {:.2f})'.format(casa/(anos*12),salario,salario*30/100))
