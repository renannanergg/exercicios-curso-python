from datetime import date
# Descobrir o ano, idade e colocar a idade para alistamento
nasc= int(input('Digite o ano de nascimento: '))
idade= (date.today().year - nasc)
# Condicionais para se ele ainda vai,ja foi ou se esta na hora de se alistar
if idade < 18:
    print('Ainda faltam \033[01;34m{}\033[m anos para voce se alistar'.format(18-idade))
    print('Seu ano de alistamento será em \033[1;34m{}\033[m'.format(nasc + 18))
elif idade == 18:
    print('Esta na hora de se alistar ! ')
    print('Seu ano de alistamento é \033[1;32m{}\033[m'.format(date.today().year))
else:
    print('Ja fazem \033[01;31m{}\033[m anos que você se alistou '.format(idade-18))
    print('Seu ano de alistamento foi em \033[1;33m{}\033[m'.format(nasc+18))
print('Quem nasceu em \033[7;30;107m{}\033[m tem \033[1;33m{}\033[m anos'.format(nasc,idade))


