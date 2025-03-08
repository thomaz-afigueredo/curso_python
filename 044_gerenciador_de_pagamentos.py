# 44: Elabore um programa que calcule o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
# à Vista dinheiro/Pix: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço normal
# 3x ou mais: 20% de juros
print('{:=^40}'.format(' LOJAS GUANABARA '))
valor = float(input('Qual o valor do produto? R$ '))
print('''Qual método de pagamento?
[ 1 ] À Vista no PIX ou Dinheiro
[ 2 ] À Vista no cartão
[ 3 ] Em até 2x no cartão
[ 4 ] 3x ou mais''')
tipo_pagamento=int(input('Sua opção: '))
if tipo_pagamento == 1:
    total = valor - (valor*10) / 100
elif tipo_pagamento == 2:
    total = valor - (valor * 5) / 100
elif tipo_pagamento == 3:
    total = valor
    print('Sua compra será parcelada em 2x de R$ {:.2f} SEM JUROS'.format(total/2))
elif tipo_pagamento == 4:
    total = valor + (valor*10) / 100
    totalparcelas=int(input('Quantas parcelas?'))
    parcela= total / totalparcelas
    print('Sua compra será parcelada em {}x de R$ {:.2f} COM JUROS'.format(totalparcelas,parcela))
print('Sua compra de R$ {:.2f} vai custar R$ {:.2f} no final'.format(valor, total))