num = 2
nomes = []
notas = []
medias = 0

for i in range(num):
    nomes.append(input('nomes: '))
    notas.append(float(input('notas: ')))
    medias = medias + notas[i]

medias = medias / num
print('A média da turma é {}'.format(medias))

for i in range(num):
    if notas[i] > medias:
        print('Parabens {}'.format(nomes[i]))
