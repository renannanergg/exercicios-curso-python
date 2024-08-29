name = input('Qual seu nome ? ').strip().title()
idade = input('Quantos anos você tem ? ').strip()
vulgo = input('Qual seu vulgo ? ').strip().title()
# Criando biblioteca de cores
cores = {'limpa':'\033[m',
         'vermelho':'\033[1;31m',
         'amarelo':'\033[1;33m',
         'azul':'\033[1;34m'}
print('-=-'*30)
print('Seu nome é {}{}{} !'.format(cores['vermelho'],name,cores['limpa']))
print('Você tem {}{}{} anos !'.format(cores['amarelo'],idade,cores['limpa']))
print('Seu apelido é {}{}{} !'.format(cores['azul'],vulgo,cores['limpa']))

