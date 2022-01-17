A = int(input())

m1,m2 = 0,0
soma_media = 0

while A > 0:
    if m1 >= 0 and m2 >= 0:
        m1 = float(input())
        m2 = float(input())
        media = (m1 + m2) / 2
        soma_media =  media + soma_media
        A = A - 1
print('%.2f' %soma_media)









