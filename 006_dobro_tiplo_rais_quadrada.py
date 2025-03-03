#Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
valor=int(input('Insira o valor de investimento'))
valor_dobro=valor*2
valor_tripo=valor*3
valor_raiz_quadrada=valor**0.5
print('Com {} você conseguirá um lucro de {}, o dobro do valor!'.format(valor,valor_dobro))
print('Ou até mesmo {}, o triplo do investido.\nRaiz quadrada fds {:.2f}'.format(valor_tripo,valor_raiz_quadrada))

