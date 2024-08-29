dado=list()
galera=list()
maisleve=0
maispesado=0
while True:
    dado.append(str(input('Nome: ')).strip().title())
    dado.append(float(input('Peso(KG): ')))
    if len(galera)==0:
        maisleve=dado[1]
        maispesado=dado[1]
    else:
        if dado[1]> maispesado:
            maispesado=dado[1]
        if dado[1]< maisleve:
            maisleve=dado[1]
    galera.append(dado[:])
    dado.clear()
    resp=str(input('Continuar? [S/N] ').strip().upper())
    while resp not in 'SN':
        resp=str(input('ERRO! Continuar?? [S/N] ').strip().upper())
    if resp=='N':
        break
print('=-='*10)
print(f'Foram cadastrados {len(galera)} pessoas.')
for p in galera:
    if p[1] == maispesado:
        print(f'{p[0]} é o mais pesado com {p[1]}kg')
for p in galera:
    if p[1] == maisleve:
        print(f'{p[0]} é o mais leve com {p[1]}kg')


        