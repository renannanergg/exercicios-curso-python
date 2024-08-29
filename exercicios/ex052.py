num= int(input('Digite um numero: '))
div=0
for c in range(1,num+1):
    if num % c ==0:
        print('\033[1;34m',end=' ')
        div = div + 1
    else:
        print('\033[1;31m',end=' ')
    print(c,end=' ')
print('\n\033[mO numero \033[1;33m{}\033[m foi divisivel \033[1;33m{}\033[m vezes\033[m'.format(num,div))
if div == 2:
    print('\n\033[mO numero {} é primo\033[m'.format(num))
else:
    print('\n\033[mO numero {} não é primo\033[m'.format(num))


