n1 = int(input())
n2 = int(input())
n3 = int(input())

s = 0

if (n1 != n2 and n1 != n3):
    s += n1

if (n2 != n1 and n2 != n3):
    s += n2

if (n3 != n1 and n3 != n2):
    s += n3

print(s)














