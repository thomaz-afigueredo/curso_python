# Exercício Python 048: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.
soma = 0
for c in range (0,501):
    if c % 3 == 0:
        soma = soma + c
print(soma)