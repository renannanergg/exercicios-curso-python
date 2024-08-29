tabelabr= ('São Paulo FC','Internacional','Palmeiras','Flamengo','Athletico-PR','Atletico-MG','Fluminense','Gremio'
           ,'Bahia','Fortaleza','Vasco','Chapecoense','Red Bull','Botafogo','Cruzeiro','Cuiaba','Criciuma','Atletico-GO',
           'Corinthians','Vitoria')
g5= (tabelabr[0:6])
z4= (tabelabr[16:])
alf= (sorted(tabelabr))


print('=='*15)
print(f'O Campeão do Brasileirão foi o grandioso \033[1;34m{tabelabr[0]}\033[m')
print(f'Os 5 primeiros colocados dessa edição do Campeonato Brasileiro foram \033[1;33m{g5}\033[m')
print(f'Os times rebaixados dessa edição foram \033[1;31m{z4}\033[m')
print(f'Os times em ordem alfabética {alf}')
print(f'A chapecoense esta na posição {tabelabr.index('Chapecoense')+1}')