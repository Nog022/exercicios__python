import math

lista = []
for i in range(5):
    f = float(input())
    lista.append(f)

soma = 0
for k in range(5):
    soma += lista[k]

media = soma/5

m = 111111100000
r = 0
for j in range(5):
    d = math.fabs(lista[j] - media)
    if d < m:
        m = d
        r = lista[j]
print('%.2f'%r)    
  




