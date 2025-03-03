# Exercício Python 035: Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.
print('-=-'*10)
print('ANALISDOR DE TRIÂNGULOS')
print('-=-'*10)
a=float(input('Primeiro segmento de reta'))
b=float(input('Segundo segmento de reta'))
c=float(input('Terceiro segmento de reta'))
if a+b>c and a+c>b and b+c>a:
    print('Os segmentos acima PODEM FORMAR um triângulo')
else:print('Os segmentos acima NÃO PODEM FORMAR um triângulo')
