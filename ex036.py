# Descobrir o valor da casa, salário e qntd de prestações
vlrcasa= float(input('Qual o valor do imóvel? R$ '))
salario= float(input('Qual o seu salário ? R$ '))
qntdprest= int(input('Em quantas parcelas ? '))
# Formula prestação
vlrprest= vlrcasa/qntdprest
# Condicinal para saber se o empréstimo será aprovado
if vlrprest > salario * 30/100:
    print('Empréstimo \033[1;31mNEGADO\033[m !')
    print('O valor da parcela é de R$ {:.2f} e supera 30% da renda informada.'.format(vlrprest))
else:
    print('Emprestimo \033[1;32mAPROVADO\033[m')
    print('O valor da parcela é de R$ {:.2f}'.format(vlrprest))
    print('Obrigado por financiar conosco !')
print('Tenha um bom dia !')
