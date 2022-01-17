sal = int(input('Salário?'))
j = int(input('Classe?'))
c3 = 0
tot = 0
nome = ''
sal2 = 0.0
for i in range(1,11,1):

 if j == 1:
    sal2 = sal * 2
    nome = 'bom'

 elif j == 2:
    sal2 = sal + sal/2
    nome = 'medio'

 else:
    j == 3
    sal2 = sal
    c3 = c3 +1

 tot= tot + sal2
 print('salario=',sal2,'classe:',nome)
print('classe3=',c3,'total=',tot)

