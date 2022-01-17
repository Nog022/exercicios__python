nome_do_funcionario = input()
salario_fixo = float(input())
total_de_vendas = float(input())

if total_de_vendas > 0:
    comissao = total_de_vendas * 0.15
    salario_total = comissao + salario_fixo

    print("TOTAL = R$ %.2f" % (salario_total))

else:
    print("TOTAL = R$ %.2f" % (salario_fixo))



