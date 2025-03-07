# 43: Desenvolva uma lógica que leia o peso e altura de uma pessoa, calcule seu ICM e mostre seu status, de acordo com a
# tabela abaixo:
# abaixo de 18.5: Abaixo do peso
# Entre 18.5 e 25: peso ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade mórbida
peso=float(input('Qual seu peso? (Kg) '))
altura=float(input('Qual sua altura? (m) '))
imc=peso/(altura**2)
print('O IMC dessa pessoa é de {:.2f}'.format(imc))
if imc <= 18.5:
    print('Você está ABAIXO DO PESO ideal')
elif imc <= 25:
    print('PARABÉNS, você está na faixa de PESO NORMAL')
elif imc <= 30:
    print('Você está em SOBREPESO')
elif imc <= 40:
    print('Você está em OBESIDADE!')
elif imc > 40:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')