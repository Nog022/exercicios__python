x = 2
y = 3
s = 0

for i in range (1,21,1):
    if i % 2 == 0:
     s = s - (x/y)
     print(i,') -',x,'/',y)

    else:
        s = s + (x / y)
    print(i,') +',x,'/',y)

    x = x + 4
    y = y * 3
print('s=',s)


