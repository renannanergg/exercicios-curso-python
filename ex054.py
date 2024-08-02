from datetime import date
atual= date.today().year
totmaior=0
totmenor=0
for p in range(1,8):
    nasc=int(input('Ano de nascimento da {}º pessoa: '.format(p)))
    idade= atual-nasc
    if idade >= 18:
        totmaior = totmaior + 1
    elif idade <18:
        totmenor = totmenor + 1


print('Ao todo tivemos \033[1;31m{}\033[m pessoas maior(es) de idade'.format(totmaior))
print('E \033[1;34m{}\033[m pessoas menor(es) de idade'.format(totmenor))

