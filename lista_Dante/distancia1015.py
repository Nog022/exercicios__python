def calcular_distancia(x1,y1,x2,y2):
    conta = ((x2 - x1)**2) + ((y2 - y1)**2)
    conta = conta ** (1/2)
    return conta


#Principal
x1,y1 = map(float, input().split())
x2,y2 = map(float, input().split())

valor_final = calcular_distancia(x1,y1,x2,y2)

print("%.4f" % (valor_final))
