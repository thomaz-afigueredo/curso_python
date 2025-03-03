nick=input('Insira o seu nick')
print(nick, ', seu tipo primitivo é:',type(nick))
print('Só tem espaços?',nick.isspace())
print('É um número?',nick.isnumeric())
print('É alfabético?',nick.isnumeric())
print('É alfanumérico?',nick.isalpha())
print('Está em maísculas?',nick.isupper())
print('Está em minúsculas?',nick.islower())
print('Está captalizada?',nick.istitle())


