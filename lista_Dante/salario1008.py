numero_do_funcionario = int(input())
horas_trabalhada = int(input())
salario_do_funcionario = float(input())

salario_por_hora = horas_trabalhada * salario_do_funcionario

print("NUMBER =", numero_do_funcionario)
print("SALARY = U$ %.2f" % (salario_por_hora))

