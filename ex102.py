def fatorial(n,show=False):
    """
    -Fatorial
    User digita um valor 'n' e sera calculado sua fatorial
    param n: Numero escolhido pelo user
    para show (opicional) irá mostrar ou nao a conta
    
    """
    print('--'*15)
    if show==True:
        fatorial=n
        print(f'{n} x',end=' ')
        for c in range(n-1,0,-1):
            print(f'{c} x',end=' ')
            fatorial= fatorial * c
            c=c-1
        print(f'0 = {fatorial}')
    else:
        fatorial=n
        for c in range(n-1,0,-1):
            fatorial= fatorial*c
            c=c-1
        print(f'{fatorial}')
    print('--'*15)
print(fatorial(5,True))
help(fatorial)
    