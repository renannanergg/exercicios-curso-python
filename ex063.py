print('-=-'*20)
print('SEQUENCIA DE FIBONACCI')
print('-=-' * 20)
n= int(input('Quantos elementos deseja ver? '))
n0=0
n1=1
cont=3
while cont <= n:
    print(n0,n1,end=' ')
    n0= n0 + n1
    n1= n0 + n1
    cont = cont + 1
print('\nFIM')
