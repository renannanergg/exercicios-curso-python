print('-=-'*20)
print('              10 TERMOS DE UMA PA            ')
print('-=-'*20)
termo= int(input('Informe o primeiro termo: '))
razao = int(input('Informe a razão: '))
decimo = termo + (10 - 1) * razao

for c in range (termo,decimo + razao,razao):
   print('\033[1;34m{}\033[m'.format(c),end=' --> ')
print('\033[1;31mACABOU\033[m')
