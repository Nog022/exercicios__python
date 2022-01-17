x = int(input())
y = int(input())

contador_anos = 0

while x < y:
    x = int(x * 1.5)
    y = (y * 1.3)
    contador_anos = contador_anos + 1
print(contador_anos)