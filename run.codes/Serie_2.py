x = int(input())
a = 3
b = 7
s = x

for i in range(1,100):

    if i % 2 == 0:
        s = s - ((a * x) / b)

    else:
        s = s + ((a * x) / b)

    b += 2
    a += 5
print('%.3f'%s)
