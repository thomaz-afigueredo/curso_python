#Exercício Python 026: Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A",
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
msg=input('Insira sua mensagem').strip().lower()
print('A letra A aparece {} vezes na frasez\n'
      'A primeira letra A apareceu na {} posição\n'
      'A última letra A apareceu na posição {}'.format(msg.count('a'),msg.find('a')+1,msg.rfind('a')+1))