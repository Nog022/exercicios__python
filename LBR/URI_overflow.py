n_maximo = int(input())
P,x,Q = input().split() 

P = int(P)
Q = int(Q)
soma = 0
multi = 0
if x == '+':
    soma = P + Q
if x == '*':
    multi = P * Q

if soma > n_maximo or multi > n_maximo:
    print('OVERFLOW')

else:
    print('OK')