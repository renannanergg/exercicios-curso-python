salario= float(input('Digite o salário do funcionário: R$ '))  #descobrir o salario
if salario > 1250:    #salario maior que 1250
    aumento = salario + (salario * 10/100)
    print('O novo salario sera de R$ {:.2f}'.format(aumento))
else:    #salario menor que 1250
    aumento= salario + (salario * 15/100)
    print('O novo salário sera de R$ {:.2f}'.format(aumento))

