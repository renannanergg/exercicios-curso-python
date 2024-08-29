lista= []
r= ' '
while True:
    n= int(input('Digite um valor: '))
    lista.append(n)
    r= str(input('Deseja continuar ? [S/N] ')).strip().upper()
    while r not in 'SN':
        r= str(input('Deseja continuar [S/N] ')).upper().strip()
    if r == 'N':
        break
lista.sort(reverse=True)
print(f'Foram digitados {len(lista)} elementos ')
print(f' Em ordem decrescente {lista}')
if 5 in lista:
    print(f'O numero 5 aparece na lista na posição {lista.index(5)+1}')
else:
    print('O numero 5 não aparece na lista')