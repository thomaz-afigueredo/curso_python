#Exercício Python 012: Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
valor_produto=float(input('Qual o valor do produto?'))
desconto=(valor_produto*0.05)/2
preco_final=valor_produto-desconto
print('Nós conseguimos um desconto incrível de {}% e o valor fica por apenas R${}. Aproveite!'.format(5,preco_final))





