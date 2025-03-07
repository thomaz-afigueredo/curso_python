# 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# à Vista dinheiro/Pix: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais: 20% de juros
valor = float(input('Qual o valor do produto? R$ '))
print('''Qual método de pagamento?
[ 1 ] À Vista no PIX ou Dinheiro
[ 2 ] À Vista no cartã
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais''')
tipo_pagamento=int(input('Sua opção: '))
if tipo_pagamento == 1:
    print('Sua compra de {:.2f} vai custar {:.2f} no final'.format(valor,valor - (valor*10) / 100))
