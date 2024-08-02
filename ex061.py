n1 = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razao: '))
nt=1
termo=n1
print('-=-'*20)
while nt<=10:
    print(termo,end=' -> ')
    termo= termo + r
    nt = nt +1
print('Fim')