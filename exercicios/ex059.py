op=0
while op != 5:
    print('-=-'*20)
    n1 = int(input('Digite o primeiro numero: '))
    n2 = int(input('Digite o segundo numero: '))
    print('[1] SOMAR'
          '\n[2] MULTIPLICAR'
          '\n[3] MAIOR NUMERO'
          '\n[4] NOVOS NUMEROS'
          '\n[5] SAIR DO PROGRAMA')
    op = int(input('Digite a opção: '))
    print('-=-'*20)
    if op == 1:
        print('ESCOLHEU SOMAR')
        print('A soma entre {} e {} vale {}'.format(n1, n2, n1 + n2))
    elif op == 2:
        print('ESCOLHEU MULTIPLICAR')
        print('O produto entre {} e {} vale {}'.format(n1, n2, n1 * n2))
    elif op == 3:
        print('ESCOLHEU MAIOR')
        if n1 > n2:
            print('O maior numero é o {}'.format(n1))
        elif n2 > n1:
            print('O maior numero é o {}'.format(n2))
        else:
            print('Os numeros são iguais')
    elif op == 4:
        n1 = int(input('Digite o primeiro numero: '))
        n2 = int(input('Digite o segundo numero: '))
        print('[1] SOMAR'
              '\n[2] MULTIPLICAR'
              '\n[3] MAIOR NUMERO'
              '\n[4] NOVOS NUMEROS'
              '\n[5] SAIR DO PROGRAMA')
        op = int(input('Digite a opção: '))
print('FINALIZADO')