from random import randint
computer = randint(0, 10)
print('O computador escolheu um numero de \033[1;32m0\033[m a \033[1;32m10\033[m')
player= int(input('Tente adivinhar: '))
erros=0
while player != computer:
    if player < computer:
        print('Um pouco mais....')
    elif player > computer:
        print('Um pouco menos....')
    erros= erros +1
    print('Voce \033[1;31merrou\033[m!')
    player=int(input('Tente denovo: '))
print('-=-'*20)
print('Voce escolheu \033[1;33m{}\033[m e o computador escolheu \033[1;33m{}\033[m'.format(computer,player))
print('Voce \033[1;34mAcertou\033[m !!\nVoce precisou de \033[1;34m{}\033[m palpites para acertar!'.format(erros))