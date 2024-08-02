# importando randomizador de numeros para o pc usar no jokenpo

from random import randint
pc= randint(1,3)

# coletar a opcao do jogador (pedra,papel,tesoura)

print('-=-'*20)
print('VAMOS JOGAR JO-KEN-PO')
print('-=-'*20)
print('[1] PEDRA')
print('[2] PAPEL')
print('[3] TESOURA')
player= int(input('ESCOLHA:'))
print('-=-'*30)

# condicional para saber quem ganhou
if player == 1 and pc == 2:
    print('Voce escolheu PEDRA')
    print('O computador escolheu PAPEL ')
    print('O vencedor é: COMPUTADOR')
elif player == 1 and pc ==3:
    print('Voce escolheu PEDRA')
    print('O computador escolheu TESOURA')
    print('O vencedor é: VOCE')
elif player == 2 and pc == 1:
    print('Voce escolheu PAPEL')
    print('O computador escolheu PEDRA')
    print('O vencedor é: VOCE')
elif player == 2 and pc == 3:
    print('Voce escolheu PAPEL')
    print('O computador escolheu TESOURA')
    print('O vencedor é: COMPUTADOR')
elif player == 3 and pc == 1:
    print('Voce escolheu TESOURA')
    print('O computador escolheu PEDRA')
    print('O vencedor é : COMPUTADOR')
elif player == 3 and pc == 2:
    print('Voce escolheu TESOURA')
    print('O computador escolheu PAPEL')
    print('O vencedor é: VOCE')
else:
    print('EMPATE')
