if salario_bruto < salario_min:
    salario = salario_bruto
    salario_bruto = (salario_bruto * 2)/100
    desconto = salario - salario_bruto
    print('{}, você teve um desconto de R$ {:.2f} e o seu salario liquido é de R$ {:.2f}'.format(nome, salario_bruto, desconto))
elif salario_bruto == salario_min:
    salario = salario_bruto
    salario_bruto = (salario_bruto * 5)/100
    desconto = salario - salario_bruto
    print('{}, você teve um desconto de R$ {:.2f} e o seu salario liquido é de R$ {:.2f}'.format(nome, salario_bruto, desconto))
else:
    salario = salario_bruto
    salario_bruto = (salario_bruto * 😎 / 100
    desconto = salario - salario_bruto
    print('{}, você teve um desconto de R$ {:.2f} e o seu salario liquido é de R$ {:.2f}'.format(nome, salario_bruto,
                                                                                                 desconto))