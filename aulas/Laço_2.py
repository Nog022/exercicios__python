resp = 1
while (resp == 1):
x = int(input())

a = 4
b = 2
z = 2
soma = x

for i in range(1,2):
    soma += ((a*(x**z))/b)
    print('(',a,'*',x,'**',z,')/'.,b)
    a += 5
    b += 2*b + 1
    z += 1
print('s=' ,soma)
rsp = int(input('De novo? (1)-Sim (0)=Não'))
