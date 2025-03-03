#Exercício Python 024: Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome "SANTO".
cid=input('Insira o nome da sua cidade').strip().lower()
print(cid.split()[0]=='santo')
