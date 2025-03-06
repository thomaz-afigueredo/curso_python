# 40: Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo
# com a média atingida:
# média abaixo de 5.0: Reprovado
# média entre 5.0 e 6.9: Recuperação
# média acima de 7.0: Aprovado
n1=float(input('Qual a sua nota no primeiro semestre?'))
n2=float(input('Qual a sua nota no segundo semestre'))
media=(n1+n2)/2
print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}'.format(n1,n2,media))
if media < 5:
    print('O aluno está REPROVADO')
elif 6.9 > media >= 5:
    print('O aluno está em RECUPERAÇÃO')
else:
    print('O aluno está APROVADO')
