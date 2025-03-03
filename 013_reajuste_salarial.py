#Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario=float(input('Estamos pensando em te recompensar com um aumento. Qual é o seu salário atualmente?'))
valor=(salario*0.15)/2
aumento=salario+valor
print('Então você vai ganhar um aumento de R${}! Agorá seu salário é de R${} Parabéns pelo compromisso com a velocidade e a qualidade das entregas! Vamos juntos!'.format(valor,aumento))
