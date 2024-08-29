print('=='*20)
print('           LOJAS RENUNCIAS          ')
print('=='*20)
totalpr=totalp=pcaro=pbarato=0
nomebarato=' '
while True:
    nomeprdt= str(input('Nome do produto: ')).title().strip()
    preco= float(input('Preço (R$): '))
    resp= ' '
    totalpr= totalpr + preco
    totalp= totalp + 1
    while resp not in 'SN':
        resp= str(input('Deseja continuar ? [S/N] ')).strip().upper()[0]
    if resp=='N':
        break
    if preco > 1000:
        pcaro = pcaro + 1
    if totalp ==1:
        nomebarato= nomeprdt
        pbarato = preco
    else:
        if preco < pbarato:
            pbarato= preco
            nomebarato= nomeprdt
print('=='*20)
print(f'O produto mais barato foi {nomebarato} que custou R${pbarato}')
print(f'O total gasto na compra foi de {totalpr} com {totalp} produtos')
print(f'Tiveram {pcaro} produtos acima de R$1000,00')