n1 = int(input('Primeiro termo: '))
razao = int(input('Razao: '))
termo= n1
cont=1
total=0
mais=10
while mais !=0:
    total = total + mais
    while cont<=total:
        print('{}'.format(termo),end=' -> ')
        termo = termo + razao
        cont= cont + 1
    print('PAUSA')
    mais= int(input('Quantos termos a mais? '))
print('Foram mostrados {} termos no total'.format(total))
