from time import sleep
def contador(i,f,p):
     if p<0:
        p *= -1
     if p ==0:
        p=1 
     print(f'Contador de {i} ate {f} de {p} em {p}')
     if i < f:
        c=i
        while c <=f:
            print(f'{c}',end=' ',flush=True)
            sleep(0.5)
            c= c + p
        print('FIM')
     else:
        c=i
        while c >=f:
            print(f'{c}',end=' ',flush=True)
            sleep(0.5)
            c=c-p
        print('FIM')


#Principal
contador(1,10,1)
contador(10,0,2)
contador(i=int(input('INICIO: ')),f=int(input('FIM: ')),p=int(input('PASSO: ')))