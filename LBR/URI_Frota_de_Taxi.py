a,g,ra,rg = map(float, input().split())

gasolina = g/rg
alcool = a/ra

if gasolina > alcool:
    print('A')

elif alcool > gasolina or alcool == gasolina:
    print('G')
