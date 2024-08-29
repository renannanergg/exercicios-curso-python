valores=[]
pares= []
impares=[]
r= ' '
while True:
    n= int(input('Digite um valor: '))
    valores.append(n)
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)
    r= str(input('Deseja continuar ? [S/N]')).upper().strip()
    while r not in 'SN':
        r= str(input('Deseja continuar ? [S/N]')).upper().strip()
    if r == 'N':
        break

print(f'A lista completa é {valores}')
print(f'Os valores pares são {pares}')
print(f'Os valores impares são {impares}')