#Exercício Python 019: Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
#Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
import random
a1=(input('Para sortear um aluno para apagar o quadro, insira o nome do primeiro:'))
a2=(input('Insira o nome do segundo aluno:'))
a3=(input('Agora, insira o nome do terceiro aluno:'))
a4=(input('Insira o nome do último aluno a ser sorteado:'))
nomes=[a1,a2,a3,a4]
print(random.choice(nomes))