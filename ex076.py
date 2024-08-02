print('--=--'*10)
print('              LISTA DE PREÇOS              ')
print('--=--'*10)
precos= ('Lápis','1,90',
         'Lapiseira','5,00',
         'Estojo','8,50',
         'Borracha','0,50',
         'Caderno','18,90',
         'Calculadora','59,90')
for pos in range(0,len(precos)):
    if pos % 2 ==0:
        print(f'{precos[pos]:.<30}',end=' ')
    else:
        print(f'R${precos[pos]:>5}')
print('--=--'*10)