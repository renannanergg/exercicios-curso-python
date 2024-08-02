num1 = int(input('Digite o primeiro numero: '))
num2 = int(input('Digite o segundo numero: '))
if num1 > num2:
    print('O numero \033[1;31m{}\033[m é maior que o numero \033[1;34m{}\033[m'.format(num1,num2))
elif num2 > num1:
    print('O numero \033[1;34m{}\033[m é maior que o numero \033[1;31m{}\033[m'.format(num2,num1))
else:
    print('Os numeros são iguais')
