bandeja = int(input())
quebrado = 0
for i in range(bandeja):    
    lata,copo = map(int, input().split())
    if lata > copo:
        quebrado += copo
print(quebrado)
    