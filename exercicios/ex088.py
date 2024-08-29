from random import randint 
njg=int(input('Quantos jogos quer que eu sorteie? '))
jogos=[]
jogo=[]
temp=[]
c=0
for c in range(0,njg):
    jogo.append(randint(0,60))
    jogo.append(randint(0,60))
    jogo.append(randint(0,60))
    jogo.append(randint(0,60))
    jogo.append(randint(0,60))
    jogo.append(randint(0,60))
    jogo.sort()
    temp.append(jogo[:])
    jogos.append(temp[:])
    temp.clear()
    jogo.clear()
    print(f'Jogo {c+1} :{jogos[c]}')
