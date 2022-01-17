a = int(input())
b = int(input())
c = int(input())

totalA = (c*4)+(b*2)
totalB = (a*2)+(c*2)
totalC = (a*4)+(b*2)
lista = []
lista.append(totalA)
lista.append(totalB)
lista.append(totalC)

tempo = min(lista)
print(tempo)