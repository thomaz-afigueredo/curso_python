# Exercício Python 033: Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
a=int(input('Insira o primeiro valor:'))
b=int(input('Insira o segundo valor:'))
c=int(input('Insira o terceiro valor:'))
#maior
maior=a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
#menor
menor=a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print('O maior valor é: {}\n'
      'O menor valor e: {}'.format(maior,menor))

