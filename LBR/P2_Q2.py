#26 letras minusculas
entrada = list(map(str, input())) 
#alfabeto
alfabeto = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z'] 
#mensagem secreta
mensagem = list(map(str, input())) 
descodificado = []
for j in range(len(mensagem)):
    for i in range(len(entrada)):
        if mensagem[j] == entrada[i]:
            descodificado.append(alfabeto[i])
#tirando os espaços
descodificação_total = ''.join(descodificado)
print(descodificação_total)    