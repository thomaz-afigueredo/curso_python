# Exercício Python 034: Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento.
# Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.
s=float(input('Qual o seu salário?'))
if s <= 1250:
    d10=s*10/100
    print('Seu aumento será de 10% no valor de R${:.2f} e seu salário será R${:.2f}'.format(d10,s+d10))
else:
    d15=s*15/100
    print('Seu aumento será de 15% no valor de R$ {:.2f} e seu salário será de {:.2f}'.format(d15,s+d15))