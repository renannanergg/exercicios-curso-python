print('=='*10)
print('{:^20}'.format('BANKONCIOS'))
print('=='*10)
saque= int(input('Valor do saque: R$'))
notas50= saque //50
restante= saque - (notas50*50)
notas20= restante//20
restante= restante - (notas20*20)
notas10= restante//10
restante= restante - (notas10*10)
notas1= restante//1
restante= restante - (notas1*1)
print('=='*10)
if notas50>0:
    print(f'Total de cédulas de 50: {notas50}')
if notas20>0:
    print(f'Total de cédulas de 20: {notas20}')
if notas10>0:
    print(f'Total de cédulas de 10: {notas10}')
if notas1 >0:
    print(f'Total de notas de 1: {notas1}')
print('=='*10)
