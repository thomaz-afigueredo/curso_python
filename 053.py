# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
f = input('Insira uma frase: ').strip().lower()
fseparado = f.split()
fjunto = ''.join(fseparado)
print(fjunto)