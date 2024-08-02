totidade=0
olderm=0
wmenorvinte=0
for pes in range (1,5):
    nome= str(input('Digite o nome da {}º pessoa: '.format(pes))).capitalize()
    idade= int(input('Digite a idade da {}º pessoa: '.format(pes)))
    sexo= str(input('Digite o sexo da {}º pessoa [M]/[F]: '.format(pes))).capitalize()
    print('-=-'*10)
    totidade= totidade + idade
    media= totidade/4
    if sexo == 'M' and pes==1:
        older= idade
        nomeolder= nome
    if sexo =='M' and idade > older:
        older= idade
        nomeolder= nome
    if sexo == 'F' and idade < 20:
        wmenorvinte= wmenorvinte + 1

print('A media de idade é de \033[1;34m{}\033[m anos'.format(media))
print('O homem mais velho tem \033[1;32m{}\033[m anos e se chama \033[1;32m{}\033[m'.format(older,nomeolder))
print('Existem \033[1;33m{}\033[m mulheres menores de 20 anos'.format(wmenorvinte))