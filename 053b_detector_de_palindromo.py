# Exercício Python 053: Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.
f = input('Insira uma frase: ').strip().lower()
fseparado = f.split()
fjunto = ''.join(fseparado)
inverso = fjunto[::-1]
if inverso == fjunto:
    print('Temos um PALÍNDROMO')
else:
    print('A frase digitada NÃO É UM PALÍNDROMO')
print('-=-'*12)
print(f , fjunto , inverso)
