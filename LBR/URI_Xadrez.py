L = int(input())
C = int(input())
s = L + C
# 1 = branca, 2 preta
for i in range(1):
    if s % 2 == 0:
        print(1)
    else:
        print(0)    

