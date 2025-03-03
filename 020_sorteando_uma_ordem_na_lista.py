#Exercício Python 020: O mesmo professor do desafio 019 quer sortear a ordem de apresentação de trabalhos dos alunos.
#Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
import random
a1=(input('Para sortear um aluno para apagar o quadro, insira o nome do primeiro:'))
a2=(input('Insira o nome do segundo aluno:'))
a3=(input('Agora, insira o nome do terceiro aluno:'))
a4=(input('Insira o nome do último aluno a ser sorteado:'))
nomes=a1,a2,a3,a4
print(random.sample(nomes,k=4))
