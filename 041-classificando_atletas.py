# 41: A confederação nacional de natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# até 9 anos: mirim
# até 14 anos: infantil
# até 19 anos: junior
# até 25 anos: sênior
# acima: Master

from datetime import date

ano_nasc=int(input('Ano de nascimento'))

idade = date.today().year - ano_nasc

print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: Mirim')
elif idade <= 14:
    print('Classificação: Infatil')
elif idade <= 19:
    print('Clssificação Junior')
elif idade <= 25:
    print('Classificação: Sênior')
else:
    print('Classificação: Master')