totn=0
soman=0
while True:
    n=int(input('Digite um numero [999 para parar]: '))
    if n == 999:
        break
    totn= totn +1
    soman= soman + n
print(f'Foram digitados {totn} numeros, totalizando {soman}')
