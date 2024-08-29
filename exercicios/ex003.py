print('Ola, bem vindo ao somador de números!')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
# Criando biblioteca de cores
cores= {'azul':'\033[34m',
        'vermelho':'\033[31m',
        'verde':'\033[32m',
        'limpa':'\033[m'}
print('A soma de {}{}{} com {}{}{} '.format(cores['azul'],n1,cores['limpa'],cores['vermelho'],n2,cores['limpa']))
print('É igual a {}{}{}'.format(cores['verde'],s,cores['limpa']))
