def leiaint(msg):
    valor=0
    while True:
        n=str(input(msg))
        if n.isnumeric():
            valor=int(n)
            break
        else:
            print('\033[0;31mErro ! Digite um numero válido\033[m')
    return valor
        
   
#Principal
n=leiaint('Digite um numero: ')
print(f'Voce acabou de digitar o numero {n}')