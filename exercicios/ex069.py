mais18=0
toth=0
mmenor20=0
while True:
    print('=='*10)
    print('CADASTRO DE PESSOAS')
    print('=='*10)
    idade= int(input('Idade: '))
    sexo= ' '
    while sexo not in 'MF':
        sexo= str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('~~'*10)
    if sexo=='M':
        toth= toth + 1
    if idade >= 18:
        mais18= mais18 + 1
    if sexo =='F' and idade <20:
        mmenor20= mmenor20 + 1
    continuar= ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N]: ')).strip().upper()[0]
    if continuar == 'N':
        break
print(f'Foram cadastradas o total de {mais18} pessoas maiores de 18 anos')
print(f'Foram cadastradas o total de {toth} homens')
print(f'Foram cadastrados {mmenor20} mulheres menores de 20 anos')



