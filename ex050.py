# Requisitar os 6 numeros e criar o somador de numeros pares e impares
sp= 0
si= 0
cont= 0
for n in range (0,6):
    inteiro= int(input('Digite um numero inteiro: '))
    if inteiro % 2 == 0:
        sp = sp + inteiro
        cont= cont + 1
    else:
        si = si + inteiro
        cont= cont + 1
print('-=-'*20)
print('Voce informou \033[1;33m{}\033[m numeros pares, e a soma é de \033[1;33m{}\033[m'.format(cont,sp))
print('Voce informou \033[1;31m{}\033[m numeros impares,e a soma é de \033[1;31m{}\033[m'.format(cont,si))

