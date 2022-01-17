#Função

    
    

    

#Programa principal
A,B,C = map(float, input().split())

area_do_triangulo = ((A * C) / 2)

area_do_circulo = 3.14159 * C ** 2

area_do_trapezio = ((A + B) * C) / 2

area_do_quadrado = B ** 2

area_do_retangulo = A * B


print("TRIANGULO: %.3f" %(area_do_triangulo))
print("CIRCULO: %.3f" %(area_do_circulo))
print("TRAPEZIO: %.3f" %(area_do_trapezio))
print("QUADRADO: %.3f" %(area_do_quadrado))
print("RETANGULO: %.3f" %(area_do_retangulo))







