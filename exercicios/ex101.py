def voto(ano):
    from datetime import datetime
    atual= datetime.today().year
    idade=atual-ano
    if idade >=18 and idade <65:
        return f'Voce tem {idade} anos, voto OBRIGATÓRIO'
    elif idade <18 and idade >16:
        return f'Voce tem {idade} anos, voto OPICIONAL'
    elif idade <16:
        return f'Voce tem {idade} anos, voto NEGADO'
    elif idade >65:
        return f'Voce tem {idade} anos, voto OPICIONAL'
        


#Principal
voto(int(input('Em que ano você nasceu? ')))
