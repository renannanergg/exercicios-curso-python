num = int(input('Digite um número: '))
print('''Escolha uma das bases para conversão: 
[1] Converter para Binário
[2] Converter para Octal
[3] Converter para Hexadecimal''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para binário é {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))
else:
    print('Opção inválida, tente novamente !')

