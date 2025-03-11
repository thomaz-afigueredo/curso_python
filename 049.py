# Exercício Python 049: Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = float(input('Qual tabuada de multiplicação vamos ver hoje?'))
for c in range (0,11):
    print(num, c , num * c)