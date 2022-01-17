n = int(input())
m = int(input())

div = 0


for i in range(1,n+1):


    for j in range(1,m+1):

        p1 = (i ** 2) * j
        p2 = (3 ** i) * (j * (3 ** i) + i * (3 ** j))
        div += p1/p2
print('%.4f' %div)