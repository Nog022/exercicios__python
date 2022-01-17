#def calcular_o_maior(calculando_AB,C):
   # if calculando_AB > C:
    #    return calculando_AB

    #else:
     #   return C

      
def calcular_maiorABC(A,B,C):
    calculando_AB = ((A + B) + abs(A - B))/2

    calculando_ABC = ((calculando_AB + C) + abs(calculando_AB - C)) /2
    
    #ABC = calcular_o_maior(calculando_AB,C)
    return calculando_ABC


#Programa Principal
A,B,C = map(int, input().split())

MaiorABC = calcular_maiorABC(A,B,C)

print("%.0f eh o maior" % (MaiorABC))
