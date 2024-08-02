n=(int(input('Digite um numero: ')),int(input('Digite outro numero: ')),int(input('Digite mais um numero: '))
       ,int(input('Digite o ultimo numero: ')))
print(n)
print(f'O numero 9 apareceu {n.count(9)} vezes')
if 3 in n:
       print(f'O numero 3 apareceu na posição {n.index(3)}')
else:
       print(f'O numero 3 não apareceu')
print(f'Os valores pares digitados são: ',end=' ')
for c in n:
       if c % 2==0:
              print(c,end=' ')

