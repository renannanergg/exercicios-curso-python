from random import randint
totv=0
derrota= False
print('-=-'*15)
print('       Vamos jogar PAR ou IMPAR     ')
print('-=-'*15)
while True:
    pcnum= randint(0,10)
    playernum= int(input('Escolha um numero: '))
    playeresc= str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    while playeresc not in 'PI':
        playeresc=str(input('Par ou Impar? [P/I] ')).upper().strip()[0]
    print('-=-'*20)
    if playeresc =='I':
        pcesc='P'
    else:
        pcesc='I'
    total= playernum + pcnum
    print(f'Voce jogou {playernum} e o computador jogou {pcnum}\nTotal de {total}')
    print('-=-'*20)
    if playeresc == 'P' and total % 2 ==0:
        print('DEU PAR')
        print('VOCE GANHOU')
        print('-=-'*20)
        totv= totv + 1
    if playeresc == 'I' and total % 2 ==1:
        print('DEU IMPAR')
        print('VOCE GANHOU')
        print('-=-'*20)
        totv= totv+1
    if pcesc == 'P' and total % 2==0:
        print('DEU PAR')
        print('VOCE PERDEU')
        derrota= True
    if pcesc == 'I' and total %2==1:
        print('DEU IMPAR')
        print('VOCE PERDEU')
        derrota= True
    if derrota == True:
        break
print('-=-'*20)
print('GAME OVER')
print(f'Voce ganhou {totv} vez(es)')


