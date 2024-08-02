from random import randint
from time import sleep
from operator import itemgetter
sorteio={'jogador#1': randint(1,6),
         'jogador#2': randint(1,6),
         'jogador#3': randint(1,6),
         'jogador#4': randint(1,6)}
ranking=list()
print('Valores sorteados: ')
for k, v in sorteio.items():
    print(f'O {k} tirou {v} no dado')
    sleep(0.5)
ranking = sorted(sorteio.items(),key=itemgetter(1),reverse=True)
print('=-='*10)
print('RANKING DOS JOGADORES')
c=1
for k,v in ranking:
    print(f'O {c}º colocado foi o {k} que tirou {v}')
    c=c+1
    sleep(0.5)