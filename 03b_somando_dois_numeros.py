gatos=int(input('Quantos gatos você tem?'))
cachorros=int(input('E quantos cachorros?'))
soma_gatos_cachorros=gatos+cachorros

#print('Legal! A soma entre',gatos,'gato(s) e',cachorros,'cachorro(s) é igual a',soma_gatos_cachorros,'pets!') --> modo antigo do Python (Python2)
print('Legal! A soma entre {} gato(s) e {} cachorro(s) é igual a {}!'.format(gatos, cachorros, soma_gatos_cachorros))

