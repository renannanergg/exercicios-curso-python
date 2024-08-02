from time import sleep
from math import factorial
numero= int(input('Digite um numero: '))
print('Calculando fatorial.....')
sleep(2)
cont= numero - 1
print('\033[1;34m{}\033[m'.format(numero),end=' ')
while cont >= 1:
    print('x \033[1;34m{}\033[m'.format(cont),end=' ')
    cont=cont-1
print('=',end=' ')
print(factorial(numero))
