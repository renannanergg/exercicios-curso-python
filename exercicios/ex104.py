def ficha(jogador=None,gols=None):
    #jogador=str(input('Nome do jogador: ').capitalize().strip())
    #gols=str(input('Gols: ').strip())
    if jogador =='':
        jogador='<desconhecido>'
    if gols=='':
        gols=0
    print(f'O jogador {jogador} marcou {gols} gols')


ficha('renan',10)