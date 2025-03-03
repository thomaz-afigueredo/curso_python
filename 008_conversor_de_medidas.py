#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
toalha_m=float(input('Quantos metros possui a toalha bordada?'))
toalha_cm=toalha_m*100
toalha_mm=toalha_m*1000
print('Isso é {:.0f}cm ou {:.0f}mm bordados, sabia?'.format(toalha_cm,toalha_mm))
