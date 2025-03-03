#Exercício Python 022: Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
fullname=input('Insira seu nome completo').strip()
splitname=fullname.split()
joinname=''.join(splitname)
print('Seu nome em letras maiúsculas é {} \n'
      'Seu nome em letras minúsculas é {}\n'
      'Seu nome tem ao todo {} letras\n'
      'Seu primeiro nome é {} e ele tem {} letras.\n'.format(fullname.upper(),fullname.lower(),len(joinname),splitname[0],len(splitname[0])))

