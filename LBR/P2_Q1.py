n,c,m = map(int, input().split()) #numero de volumes lançados #comemorativos #ja_comprados

vol_comemorativo =  list(map(int, input().split())) #volumes comemoratvios  

ja_tem = list(map(int, input().split()))

v = c + m
cont = 0
for j in range(len(vol_comemorativo)):
    for i in range(len(ja_tem)):
        if ja_tem[i] == vol_comemorativo[j]:
            cont += 1 
            break

if cont < c:
    falta = c - cont
    print(falta)

else:
    print('0')