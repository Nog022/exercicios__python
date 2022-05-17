#Dicionario

dicionario = {}
dicionario2 = dict()

familia = {'Pai': 'Roberto', 'Mãe': 'bianca', 'TemFilhos':False}

familia2 = dict(Pai= "Carlos", Mae= "Maria", TemFilhos= False)

listas_tuplas = [('Pai','Roberto'),('Mãe','bianca'),('TemFilhos',False)]

familia3 = dict(listas_tuplas)

#para saber os elementos de um dicionario usa-se aspas print(familia2['Pai'])

#para saber as chaves (.keys()) e para os valores dentro das chave (values.())

#Adicionando um elemento
familia2['Cachorro'] = 'Luck'

#Adicionando varios elementos
familia2.update({'Casa':False, 'Carro':True})

#excluido elementos
familia2.pop('Carro')

#exlcuindo elemento
del familia2['Casa']

#Trocando elemento
familia2['Cachorro'] = 'Tedy'

#vendo se existe uma chave ou valor dentro do dicionario 
'Mae' in familia2

#Colocando uma lista dentro um dicionario 
familia2['Animais'] = {'Cachorro', 'Gato', 'Passarinho'}

#print(familia2)

#Funções

def um():
    x = 1
    print(x)
    dois(x)
    print(x)

def dois(y):
    print(y)
    y = 2
    print(y)