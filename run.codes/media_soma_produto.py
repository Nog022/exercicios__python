n1 = int(input())
n2 = int(input())
n3 = int(input())

m = (n1 + n2 + n3) / 3
s = n1 + n2 + n3
p = n1 * n2 * n3
print('%.1f'%m)
print(s)
print(p)

if (n1 < n2 and n1 < n3):
    print(n1)

elif (n2 < n3):
    print(n2)

else:
    print(n3)

if (n1 > n2 and n1 > n3):
    print(n1)

elif (n2 > n3):
    print(n2)

else:
    print(n3)
