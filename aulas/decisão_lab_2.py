sb = float(input())


if (sb >= 500 and sb < 800):
    desconto1 = ((sb * 10) / 100)
    sl = sb - desconto1
    print(sl)

elif (sb >= 800 and sb < 1000):
    desconto2 = ((sb * 15) / 100)
    sl = sb - desconto2
    print(sl)

elif (sb >= 1000):
    desconto3 = ((sb * 80) / 100)
    sl = sb - desconto3
    print(sl)

else:
    (sb < 500)
    print(sb)