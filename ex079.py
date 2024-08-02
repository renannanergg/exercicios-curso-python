valores= []
while True:
    n = int(input('Digite um valor: '))
    if n not in valores:
        valores.append(n)
    else:
        print('Valor duplicado, NÃO SERÁ ADICIONADO')
    resp = str(input('Quer continuar? [S/N] ')).upper().strip()
    while resp not in 'SN':
        resp= str(input('Quer continuar? [S/N] ')).upper().strip()
    if resp == 'N':
        break
print('=='*10)
print(f'Os valores digitados foram {sorted(valores)}')
