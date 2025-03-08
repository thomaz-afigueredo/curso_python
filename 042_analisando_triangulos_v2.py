# 42: Refaça o desafio 35 dos triangulos, acrescetando o recurso de mostrar que tipo de triângulo será formado:
# Equilátero: Todos os lados iguais
# Isósceles: Dois lados iguais
# Escaleno: Todos os lados diferente.

# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-'*10)
print('ANALISDOR DE TRIÂNGULOS')
print('-=-'*10)
a=float(input('Primeiro segmento de reta'))
b=float(input('Segundo segmento de reta'))
c=float(input('Terceiro segmento de reta'))
if a + b > c and a + c > b and b + c > a:
    print('Os segmentos acima PODEM FORMAR um triângulo ',end='')
    if a == b and b == c:
     print('EQUILÁTERO')
    elif a != b and a != c and b != c:
     print('ESCALENO')
    else:
        print ('ISÓSCELES')
else:
    print('Os segmentos acima NÃO PODEM FORMAR um triângulo')