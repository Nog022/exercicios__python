n1 = int(input())
n2 = int(input())
n3 = int(input())

par = n1 + n2 + n3
s = 0
m = 0

if n1 + n2 == n3:
    s += n3
    print('soma')

elif n3 + n1 == n2:
    s += n2
    print('soma')

elif n2 + n3 == n1:
    s += n1
    print('soma')


elif (n1 * n2) == n3:
    m += n3
    print('multi')

elif (n3 * n1) == n2:
    m += n2
    print('multi')

elif (n2 * n3) == n1:
    m += n1
    print('multi')

elif par % 2 == 0:
    print('par')

else:
    print('ímpar')






