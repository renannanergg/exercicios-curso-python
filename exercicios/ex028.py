import random
# from random import randint
nome= str(input('Qual é seu nome ? ')).strip().title()
print ('Muito prazer {}, vou pensar em um número de 0 a 5, consegue adivinhar ?  '.format(nome))
numr= random.randint(0,5) #pensar num numero aleatorio
numu= int(input('Digite um numero: ')) #pedir o usuario adivinhar o numero
print('-=-'*20)
if numu == numr: #se o numero digitado for igual ao pensado
    print('Parábens voce acertou !')
else: #se o numero for diferente do pensado
    print('Infelizmente voce errou')
print('O numero que eu pensei foi {}'.format(numr))
