#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1=float(input('Qual foi a sua nota no primeiro semestre?'))
nota2=float(input('E no sugundo semestre, qual sua nota?'))
media=(nota1+nota2)/2
print('Meu caro aluno, sua média é {:.1f}.'.format(media))