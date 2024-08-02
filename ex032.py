from datetime import date      #importat biblioteca de data para saber a data atual
ano= int(input('Que ano quer analisar ? Coloque 0 para analisar o ano atual:  ')) #descobrir o ano a ser analisado
if ano== 0:
    ano= date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :    #expressao para saber se o ano é bissexto
    print('O ano {} é Bissexto'.format(ano))
else:
    print('O ano {} não é bissexto'.format(ano))