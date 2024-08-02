dado = dict()
pessoas = []
tot = media = 0
while True:
    dado['nome'] = str(input('Nome: ').title().strip())
    dado['sexo'] = str(input('Sexo[F/M]: ').upper().strip())
    while dado['sexo'] not in 'FM':
        dado['sexo'] = str(
            input('ERRO !! Digite apenas [F/M]: ').upper().strip())
    dado['idade'] = int(input('Idade: '))
    resp = str(input('Continuar[S/N]: ').upper().strip())
    while resp not in 'SN':
        resp = str(input('ERRO! Digite apenas [S/N] ').upper().strip())
    pessoas.append(dado.copy())
    dado.clear()
    if resp == 'N':
        break
for p in range(len(pessoas)):
    tot = tot + pessoas[p]['idade']
media = tot/(len(pessoas))
print('=='*10)
print(f'Ao todos temos {len(pessoas)} pessoas cadastradas')
print(f'A média de idade é de {media:5.2f} anos')
print('Foram registradas as mulheres: ')
for p in range(len(pessoas)):
    if pessoas[p]['sexo'] == 'F':
        print(f'-- {pessoas[p]['nome']}')
for p in range(len(pessoas)):
    if pessoas[p]['idade'] > media:
        print(f'Acima da média: {pessoas[p]['nome']}, {pessoas[p]['sexo']} com {pessoas[p]['idade']} anos')
