n= int(input('Digite um valor: '))
an= n-1
su= n+1
# Criando Biblioteca de cores
cores= {'limpa':'\033[m',
        'preto':'\033[1;30m',
        'branco':'\033[1;97m',
        'azul':'\033[1;34m'}
print('O valor {}{}{}'.format(cores['preto'],n,cores['limpa']))
print('Seu antecessor é {}{}{}'.format(cores['branco'],an,cores['limpa']))
print('Seu sucessor é {}{}{}'.format(cores['azul'],su,cores['limpa']))