c = int(input())

matriculas = []

notas = []
for i in range(c):
    m = int(input())
    matriculas.append(m)
#print(matriculas)

for j in range(c):
    n = float(input())
    notas.append(n)
#print(notas)

for _ in range(c):
    for k in range(c-1):
        if notas[k] > notas[k+1]:
            notas[k], notas[k+1] = notas[k+1], notas[k]
            matriculas[k], matriculas[k+1] = matriculas[k+1], matriculas[k]       
             
print(matriculas)




    
        
   