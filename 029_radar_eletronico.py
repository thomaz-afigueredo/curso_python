# Exercício Python 029: Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h,
# mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.
velocidade_carro=int(input('Qual a velocidade do veículo?'))
velocidade_via=80
valor_multa=7
calc_multa=(velocidade_carro-velocidade_via)*valor_multa
if velocidade_carro > velocidade_via:
    print('Você foi multado por excesso de velocidade.\n'
          'Esta via permite trânsito até de no máximo {}km/h\n'
          'O veículo trafegava a {}km/h\n'
          'O valor da multa é de R$ {}'.format(velocidade_via,velocidade_carro,calc_multa))
else: print('O veículo trafegava a {}kh,dentro do limite da via permitida, que é de {}km/h')