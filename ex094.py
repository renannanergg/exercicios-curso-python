dados={}
jogadores=[]
gols=[]
assists=[]
while True:
    dados['jogador']=str(input('Nome do jogador: ').capitalize())
    partidas=int(input(f'Quantas partidas {dados["jogador"]} jogou na temporada? '))
    for p in range(partidas):
        gols.append(int(input(f'    Quantos gols {dados["jogador"]} marcou na partida {p+1}: ')))
        assists.append(int(input(f'    Quantas assistências {dados["jogador"]} deu na partida {p+1}: ')))
    dados['gols']=gols.copy()
    gols.clear()
    dados['assists']=assists.copy()
    assists.clear()
    dados['totgol']=sum(dados['gols'])
    dados['totassists']=sum(dados['assists'])
    dados['partgols'] = dados['totgol']+dados['totassists']
    print('=-='*10)
    print(dados)
    print('-=-'*10)
    for k,v in dados.items():
        print(f'O campo {k} tem valor {v}')
    print('-=-'*10)
    print(f'O {dados["jogador"]} jogou {partidas} partidas')
    for p in range(partidas):
        print(f'    Na partida {p+1}, fez {dados["gols"][p]} gols e deu {dados["assists"][p]} assistências')
    print('-=-'*10)
    print(f'O jogador {dados["jogador"]} participou de {dados["partgols"]} gols em {partidas} partidas durante a temporada')
    print('-=-'*10)
    resp=str(input('Continuar ?[S/N]  ').upper())
    print('-=-'*10)
    jogadores.append(dados.copy())
    dados.clear()
    if resp=='N':
        break
for j in range(len(jogadores)):
    print(f'Jogador#{j+1} {jogadores[j]["jogador"]}: {jogadores[j]}')

