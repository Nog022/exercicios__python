import math

#Largura, Altura, Profundidade da caixa,  Raio da esfera
A,B,C,D = map(int,input().split())

diametro = 2*D

D = math.sqrt((A**2)+(B**2)+(C**2))


if diametro >= D:
    print('S')

else:
    print('N')



