#Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
h=float(input('Qual a altura da parade?'))
l=float(input('Qual a lagura?'))
a=h*l # a=m²
tinta=2 # 1 tinta = 2m²
need=a//tinta
print('Sua prede tem {}x{} e possui {:.2f} de área.'.format(h,l,a))
print('Você precisará de {} baldes de tinta'.format(need))
