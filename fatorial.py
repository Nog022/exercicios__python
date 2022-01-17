num = int(input())

resultado = 1
var = 1
var2 = 2
if num == 0:
    print("1")
if num == 1:
    print("1")

for i in range(num):
    resultado = resultado * var  
    var += 1
    
    

print(resultado)