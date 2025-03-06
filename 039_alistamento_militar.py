# 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# Se ele ainda vai se alistar ao serviço militar
# Se é a hora de se alistar
# Se já passou o tempo de alisamento

from datetime import date

ano_nasc=int(input('Ano de nascimento'))

idade=date.today().year - ano_nasc

if idade < 18:
    print('Quem nasceu em {} tem {} anos em {}.\n'
          'Ainda faltam {} anos para o alistamento.\n'
          'Seu alistamento será em {}'.format(ano_nasc,idade,date.today().year,18 - idade,18 - idade + date.today().year))
elif idade == 18:
    print('Quem nasceu em {} tem {} anos em {}.\n'
          'Você tem que se alistar IMEDIATAMENTE.'.format(ano_nasc, idade, date.today().year,))
else:
    print('Quem nasceu em {} tem {} anos em {}.\n'
          'Você ja deveria ter se alistado há {} anos.\n'
          'Seu alistamento foi em {}'.format(ano_nasc, idade, date.today().year, idade - 18, 18 - idade + date.today().year))
