print('-=-'*20)
print('TABUADA')
print('-=-'*20)
while True:
    print('-=-'*20)
    n=int(input('Quer a tabuada de qual numero ? '))
    print('-=-'*20)
    if n < 0:
        break
    for cont in range (1,11):
        print (f'{n} x {cont} = {n*cont}')
        cont= cont + 1
print('Programa de Tabuada encerrado')