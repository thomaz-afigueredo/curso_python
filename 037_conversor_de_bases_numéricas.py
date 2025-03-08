#37:  Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário
# 2 para octal
# 3 para hexadecimal
n=int(input('Digite um número inteiro'))
print('''Escolha umas das bases para conversão
[ 1 ] converter para BINÁRIO
[ 2 ] convertar para OCTAL
[ 3 ] converter para HEXADECIMAL''')
opcao=int(input('Sua opção'))
if opcao == 1:
      print('{} em base BINÁRIA é: {} ou somente: {}'.format(n,bin(n),bin(n)[2:]))
elif opcao == 2:
      print ('{} em base OCTAL é: {} ou somente: {}'.format(n,oct(n),oct(n)[2:]))
elif opcao == 3:
      print('{} em base HEXADECIMAL é: {} ou somente: {}'.format(n,hex(n),hex(n)[2:]))
else: print('Opção inválida. Tente novamente')

