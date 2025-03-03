#Exercício Python 027: Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
fullname=input('Insira seu nome completo').strip().lower()
name=fullname.split()
firstname=name[0].capitalize()
lastname=name[-1].capitalize()
print('Primeiro nome: {}\n'
      'Último nome: {}'.format(firstname,lastname))