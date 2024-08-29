cont=0
totn=0
n=0
while n!=999:
    n=int(input('Digite um numero [999 para parar]: '))
    totn= totn + n
    cont=cont + 1
print('FIM')
print('Ao todos foram digitados {} numeros e a soma deles é {}'.format(cont-1,totn-999))
