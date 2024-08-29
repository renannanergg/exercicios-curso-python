km= float(input('Quantidade de KM percorridos: '))
dias= float(input('Quantidade de dias: '))
valor= (km * 0.15) + (dias * 60)
print('O total a ser pago: {:.2f}'.format(valor))